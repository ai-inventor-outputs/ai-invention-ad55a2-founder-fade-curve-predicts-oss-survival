#!/usr/bin/env python3
"""
Testing Founder Fade Curves as Predictors of OSS Survival
Full experiment implementation comparing fade curve descriptors vs static features.
Output follows exp_gen_sol_out.json schema with datasets/examples structure.
"""

import json
import sys
import warnings
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from loguru import logger
from scipy.signal import savgol_filter
from scipy.stats import pointbiserialr
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.metrics import log_loss, r2_score, roc_auc_score
from sklearn.model_selection import KFold, StratifiedKFold, cross_validate
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore", category=RuntimeWarning)

# Setup logging
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss} | {level:<7} | {message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

DATA_PATH = Path("data/data_out.json")
OUTPUT_PATH = Path("method_out.json")


@logger.catch(reraise=True)
def load_and_validate() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load and validate the dataset, returning static and time-series DataFrames."""
    logger.info(f"Loading data from {DATA_PATH}")
    
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")
    
    with DATA_PATH.open() as f:
        data = json.load(f)
    
    examples = data.get("examples", [])
    logger.info(f"Loaded {len(examples)} projects")
    
    # Build static features DataFrame
    static_rows = []
    timeseries_rows = []
    
    for ex in examples:
        project_id = ex["project_id"]
        static = ex["static_features_at_departure"]
        
        static_row = {
            "project_id": project_id,
            "founder_id": ex["founder_id"],
            "departure_date": ex["departure_date"],
            "is_survived": int(ex["survival_label"]),
            "bus_factor": static["bus_factor_at_departure"],
            "contributor_count": static["contributor_count"],
            "project_age": static["repo_age_days"] / 365.25,  # in years
            "stars": static["stars"],
            "file_count": static["file_count"],
        }
        
        # Post-departure activity (continuous target)
        post_commits = ex["post_departure_metrics"]["total_monthly_commits"]
        post_departure_activity = float(np.mean(post_commits))
        static_row["post_departure_activity"] = post_departure_activity
        
        static_rows.append(static_row)
        
        # Time-series data
        for m in ex["pre_departure_metrics"]:
            # Combined share: average of commit, merge, review shares
            combined = np.mean([
                m["founder_commit_share"],
                m["founder_merge_share"],
                m["founder_review_share"]
            ])
            timeseries_rows.append({
                "project_id": project_id,
                "month_index": m["month_index"],
                "founder_commit_share": m["founder_commit_share"],
                "founder_merge_share": m["founder_merge_share"],
                "founder_review_share": m["founder_review_share"],
                "combined_share": combined,
                "total_monthly_commits": m["total_monthly_commits"],
                "total_monthly_merges": m["total_monthly_merges"],
            })
    
    df_static = pd.DataFrame(static_rows)
    df_ts = pd.DataFrame(timeseries_rows)
    
    logger.info(f"Static shape: {df_static.shape}, Time-series shape: {df_ts.shape}")
    logger.info(f"Survival distribution: {df_static['is_survived'].value_counts().to_dict()}")
    
    # Validate
    assert df_static["project_id"].nunique() == len(df_static), "Duplicate project_ids"
    assert df_ts["project_id"].isin(df_static["project_id"]).all(), "TS project_ids not in static"
    assert df_static["is_survived"].notna().all(), "Missing survival labels"
    
    return df_static, df_ts


@logger.catch(reraise=True)
def compute_descriptors(group: pd.DataFrame) -> pd.Series:
    """
    Compute fade curve descriptors for a single project's time-series.
    
    Returns: slope, convexity, decline_start, cliff_score, is_plateau, fade_idx
    """
    # Sort by month_index
    group = group.sort_values("month_index")
    
    t = group["month_index"].values.astype(float)
    y = group["combined_share"].values.astype(float)
    
    n = len(y)
    if n < 3:
        # Too little data - return defaults
        return pd.Series({
            "slope": 0.0,
            "convexity": 0.0,
            "decline_start": 0,
            "cliff_score": 0.0,
            "is_plateau": 0,
            "fade_idx": 0.5
        })
    
    # Step A: Denoising with Savitzky-Golay
    window_length = min(5, n // 2 * 2 - 1) or 3
    if window_length % 2 == 0:
        window_length -= 1
    window_length = max(3, window_length)
    
    try:
        y_smooth = savgol_filter(y, window_length=window_length, polyorder=min(2, window_length - 1))
    except ValueError:
        y_smooth = y.copy()
    
    # Descriptor 1: Linear Slope (S_slope)
    try:
        slope, _ = np.polyfit(t, y_smooth, 1)
    except np.linalg.LinAlgError:
        slope = 0.0
    
    # Descriptor 2: Curvature/Convexity (S_convex)
    # Mean of second derivative
    try:
        first_deriv = np.gradient(y_smooth)
        second_deriv = np.gradient(first_deriv)
        convexity = float(np.mean(second_deriv))
    except Exception:
        convexity = 0.0
    
    # Descriptor 3: Time-to-Onset-of-Decline (S_decline_start)
    # First index where derivative is consistently negative
    try:
        deriv = np.gradient(y_smooth)
        decline_indices = np.where(deriv < -0.01)[0]
        decline_start = int(decline_indices[0]) if len(decline_indices) > 0 else n
    except Exception:
        decline_start = n
    
    # Descriptor 4: Abrupt-Cliff Indicator (S_cliff)
    # Ratio of final 2-month drop to average of prior 6 months
    if n > 8:
        recent_avg = float(np.mean(y_smooth[-8:-2]))
        final_drop = recent_avg - float(np.mean(y_smooth[-2:]))
        cliff_score = max(0.0, final_drop / (recent_avg + 1e-6))
    else:
        cliff_score = 0.0
    
    # Descriptor 5: Plateau-then-Cliff (S_plateau)
    is_plateau = 0
    if len(decline_indices) > 0 and n > 10:
        idx = decline_indices[0]
        if idx > 5:
            plateau_variance = float(np.var(y_smooth[idx-5:idx]))
            total_variance = float(np.var(y_smooth))
            if plateau_variance < total_variance * 0.5 and total_variance > 0:
                is_plateau = 1
    
    # Descriptor 6: Composite Fade Index (S_fade_idx)
    # 1.0 = perfect linear smooth decline, 0.0 = sudden drop
    fade_idx = np.clip(1.0 - cliff_score + (0.5 if slope < 0 else 0), 0, 1)
    
    return pd.Series({
        "slope": float(slope),
        "convexity": float(convexity),
        "decline_start": float(decline_start),
        "cliff_score": float(cliff_score),
        "is_plateau": float(is_plateau),
        "fade_idx": float(fade_idx)
    })


@logger.catch(reraise=True)
def run_experiment(df_static: pd.DataFrame, df_ts: pd.DataFrame) -> dict[str, Any]:
    """Run the full experiment pipeline."""
    
    logger.info("Computing fade curve descriptors...")
    features_fade = df_ts.groupby("project_id").apply(compute_descriptors, include_groups=False)
    features_fade = features_fade.reset_index()
    
    df_final = df_static.merge(features_fade, on="project_id")
    logger.info(f"Merged dataset shape: {df_final.shape}")
    
    # Check for NaN values
    logger.info(f"NaN counts:\n{df_final.isna().sum()}")
    df_final = df_final.fillna(0)
    
    # Define feature sets
    static_features = ["bus_factor", "contributor_count", "project_age", "stars", "file_count"]
    fade_features = ["slope", "convexity", "decline_start", "cliff_score", "is_plateau", "fade_idx"]
    all_features = static_features + fade_features
    
    X_static = df_final[static_features].values
    X_fade = df_final[fade_features].values
    X_combined = df_final[all_features].values
    
    y_binary = df_final["is_survived"].values
    y_continuous = df_final["post_departure_activity"].values
    
    logger.info(f"Class balance: {np.bincount(y_binary)}")
    
    # Standardize features
    scaler_static = StandardScaler()
    scaler_fade = StandardScaler()
    scaler_combined = StandardScaler()
    
    X_static_scaled = scaler_static.fit_transform(X_static)
    X_fade_scaled = scaler_fade.fit_transform(X_fade)
    X_combined_scaled = scaler_combined.fit_transform(X_combined)
    
    # Cross-validation setup
    cv_binary = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_continuous = KFold(n_splits=5, shuffle=True, random_state=42)
    
    results = {}
    
    # --- Model A: Baseline (Static Only) - Logistic Regression ---
    logger.info("Training Model A: Static Only (Logistic Regression)")
    model_a = LogisticRegression(penalty="l2", C=1.0, max_iter=1000, random_state=42, class_weight="balanced")
    cv_a = cross_validate(
        model_a, X_static_scaled, y_binary,
        cv=cv_binary, scoring=["roc_auc", "neg_log_loss"],
        return_estimator=True, n_jobs=-1
    )
    results["model_a_auc"] = float(np.mean(cv_a["test_roc_auc"]))
    results["model_a_auc_std"] = float(np.std(cv_a["test_roc_auc"]))
    results["model_a_logloss"] = float(-np.mean(cv_a["test_neg_log_loss"]))
    results["model_a_logloss_std"] = float(np.std(cv_a["test_neg_log_loss"]))
    logger.info(f"  AUC: {results['model_a_auc']:.4f} ± {results['model_a_auc_std']:.4f}")
    
    # Get per-fold predictions for Model A
    model_a_probs = []
    for fold_idx, (train_idx, test_idx) in enumerate(cv_binary.split(X_static_scaled, y_binary)):
        model_a.fit(X_static_scaled[train_idx], y_binary[train_idx])
        probs = model_a.predict_proba(X_static_scaled[test_idx])[:, 1]
        for i, idx in enumerate(test_idx):
            model_a_probs.append((idx, probs[i], fold_idx))
    
    # R2 for continuous (Ridge)
    model_a_cont = Ridge(alpha=1.0, random_state=42)
    cv_a_cont = cross_validate(
        model_a_cont, X_static_scaled, y_continuous,
        cv=cv_continuous, scoring="r2", return_estimator=True, n_jobs=-1
    )
    results["model_a_r2"] = float(np.mean(cv_a_cont["test_score"]))
    results["model_a_r2_std"] = float(np.std(cv_a_cont["test_score"]))
    logger.info(f"  R2: {results['model_a_r2']:.4f} ± {results['model_a_r2_std']:.4f}")
    
    # --- Model B: Hypothesis (Fade Only) - Logistic Regression ---
    logger.info("Training Model B: Fade Only (Logistic Regression)")
    model_b = LogisticRegression(penalty="l2", C=1.0, max_iter=1000, random_state=42, class_weight="balanced")
    cv_b = cross_validate(
        model_b, X_fade_scaled, y_binary,
        cv=cv_binary, scoring=["roc_auc", "neg_log_loss"],
        return_estimator=True, n_jobs=-1
    )
    results["model_b_auc"] = float(np.mean(cv_b["test_roc_auc"]))
    results["model_b_auc_std"] = float(np.std(cv_b["test_roc_auc"]))
    results["model_b_logloss"] = float(-np.mean(cv_b["test_neg_log_loss"]))
    results["model_b_logloss_std"] = float(np.std(cv_b["test_neg_log_loss"]))
    logger.info(f"  AUC: {results['model_b_auc']:.4f} ± {results['model_b_auc_std']:.4f}")
    
    # Get per-fold predictions for Model B
    model_b_probs = []
    for fold_idx, (train_idx, test_idx) in enumerate(cv_binary.split(X_fade_scaled, y_binary)):
        model_b.fit(X_fade_scaled[train_idx], y_binary[train_idx])
        probs = model_b.predict_proba(X_fade_scaled[test_idx])[:, 1]
        for i, idx in enumerate(test_idx):
            model_b_probs.append((idx, probs[i], fold_idx))
    
    model_b_cont = Ridge(alpha=1.0, random_state=42)
    cv_b_cont = cross_validate(
        model_b_cont, X_fade_scaled, y_continuous,
        cv=cv_continuous, scoring="r2", return_estimator=True, n_jobs=-1
    )
    results["model_b_r2"] = float(np.mean(cv_b_cont["test_score"]))
    results["model_b_r2_std"] = float(np.std(cv_b_cont["test_score"]))
    logger.info(f"  R2: {results['model_b_r2']:.4f} ± {results['model_b_r2_std']:.4f}")
    
    # --- Model C: Combined - Logistic Regression ---
    logger.info("Training Model C: Combined (Logistic Regression)")
    model_c = LogisticRegression(penalty="l2", C=1.0, max_iter=1000, random_state=42, class_weight="balanced")
    cv_c = cross_validate(
        model_c, X_combined_scaled, y_binary,
        cv=cv_binary, scoring=["roc_auc", "neg_log_loss"],
        return_estimator=True, n_jobs=-1
    )
    results["model_c_auc"] = float(np.mean(cv_c["test_roc_auc"]))
    results["model_c_auc_std"] = float(np.std(cv_c["test_roc_auc"]))
    results["model_c_logloss"] = float(-np.mean(cv_c["test_neg_log_loss"]))
    results["model_c_logloss_std"] = float(np.std(cv_c["test_neg_log_loss"]))
    logger.info(f"  AUC: {results['model_c_auc']:.4f} ± {results['model_c_auc_std']:.4f}")
    
    # Get per-fold predictions for Model C
    model_c_probs = []
    for fold_idx, (train_idx, test_idx) in enumerate(cv_binary.split(X_combined_scaled, y_binary)):
        model_c.fit(X_combined_scaled[train_idx], y_binary[train_idx])
        probs = model_c.predict_proba(X_combined_scaled[test_idx])[:, 1]
        for i, idx in enumerate(test_idx):
            model_c_probs.append((idx, probs[i], fold_idx))
    
    model_c_cont = Ridge(alpha=1.0, random_state=42)
    cv_c_cont = cross_validate(
        model_c_cont, X_combined_scaled, y_continuous,
        cv=cv_continuous, scoring="r2", return_estimator=True, n_jobs=-1
    )
    results["model_c_r2"] = float(np.mean(cv_c_cont["test_score"]))
    results["model_c_r2_std"] = float(np.std(cv_c_cont["test_score"]))
    logger.info(f"  R2: {results['model_c_r2']:.4f} ± {results['model_c_r2_std']:.4f}")
    
    # --- Feature Importance (Permutation Importance on Combined Model) ---
    logger.info("Computing permutation importance...")
    model_c.fit(X_combined_scaled, y_binary)
    
    perm_importance = permutation_importance(
        model_c, X_combined_scaled, y_binary,
        n_repeats=30, random_state=42, n_jobs=-1,
        scoring="roc_auc"
    )
    
    importance_dict = dict(zip(all_features, perm_importance.importances_mean.tolist()))
    
    fade_importance = {k: v for k, v in importance_dict.items() if k in fade_features}
    static_importance = {k: v for k, v in importance_dict.items() if k in static_features}
    
    results["feature_importance"] = {
        "fade_descriptors": fade_importance,
        "static_descriptors": static_importance
    }
    logger.info(f"  Fade importance: {fade_importance}")
    logger.info(f"  Static importance: {static_importance}")
    
    # --- Directionality: Correlation between fade_idx and survival ---
    fade_idx_values = df_final["fade_idx"].values
    corr, p_val = pointbiserialr(fade_idx_values, y_binary)
    direction = "Positive" if corr > 0 else "Negative"
    results["directionality"] = f"{direction} correlation between fade_idx and survival (r={corr:.3f}, p={p_val:.3f})"
    logger.info(f"  Directionality: {results['directionality']}")
    
    # --- Falsification Control ---
    logger.info("Running falsification control...")
    np.random.seed(123)
    X_fade_shuffled = X_fade_scaled.copy()
    for col in range(X_fade_shuffled.shape[1]):
        np.random.shuffle(X_fade_shuffled[:, col])
    
    model_control = LogisticRegression(penalty="l2", C=1.0, max_iter=1000, random_state=42, class_weight="balanced")
    cv_control = cross_validate(
        model_control, X_fade_shuffled, y_binary,
        cv=cv_binary, scoring="roc_auc", n_jobs=-1
    )
    control_auc = float(np.mean(cv_control["test_score"]))
    
    auc_diff = results["model_b_auc"] - control_auc
    if auc_diff > 0.05 and results["model_b_auc"] > control_auc:
        falsification = f"Significant: Fade AUC ({results['model_b_auc']:.3f}) > Control AUC ({control_auc:.3f}), diff={auc_diff:.3f}"
    else:
        falsification = f"Not significant: Fade AUC ({results['model_b_auc']:.3f}) vs Control AUC ({control_auc:.3f}), diff={auc_diff:.3f}"
    
    results["falsification_result"] = falsification
    logger.info(f"  Falsification: {falsification}")
    
    # --- Additional: Model D - Continuous Activity Predictor ---
    logger.info("Training Model D: Continuous Activity (Ridge)")
    model_d = Ridge(alpha=1.0, random_state=42)
    cv_d = cross_validate(
        model_d, X_combined_scaled, y_continuous,
        cv=cv_continuous, scoring="r2", return_estimator=True, n_jobs=-1
    )
    results["model_d_r2"] = float(np.mean(cv_d["test_score"]))
    results["model_d_r2_std"] = float(np.std(cv_d["test_score"]))
    logger.info(f"  R2: {results['model_d_r2']:.4f} ± {results['model_d_r2_std']:.4f}")
    
    model_d_static = Ridge(alpha=1.0, random_state=42)
    cv_d_static = cross_validate(
        model_d_static, X_static_scaled, y_continuous,
        cv=cv_continuous, scoring="r2", n_jobs=-1
    )
    results["model_d_static_r2"] = float(np.mean(cv_d_static["test_score"]))
    results["model_d_static_r2_std"] = float(np.std(cv_d_static["test_score"]))
    
    model_d_fade = Ridge(alpha=1.0, random_state=42)
    cv_d_fade = cross_validate(
        model_d_fade, X_fade_scaled, y_continuous,
        cv=cv_continuous, scoring="r2", n_jobs=-1
    )
    results["model_d_fade_r2"] = float(np.mean(cv_d_fade["test_score"]))
    results["model_d_fade_r2_std"] = float(np.std(cv_d_fade["test_score"]))
    
    # Prepare examples for exp_gen_sol_out schema
    # Convert per-fold predictions to per-example format
    prob_dict_a = {idx: (prob, fold) for idx, prob, fold in model_a_probs}
    prob_dict_b = {idx: (prob, fold) for idx, prob, fold in model_b_probs}
    prob_dict_c = {idx: (prob, fold) for idx, prob, fold in model_c_probs}
    
    examples = []
    for idx in range(len(df_final)):
        project_id = df_final.iloc[idx]["project_id"]
        true_label = int(df_final.iloc[idx]["is_survived"])
        
        # Get predictions from each model
        prob_a, fold_a = prob_dict_a.get(idx, (0.5, -1))
        prob_b, fold_b = prob_dict_b.get(idx, (0.5, -1))
        prob_c, fold_c = prob_dict_c.get(idx, (0.5, -1))
        
        pred_a = "survive" if prob_a > 0.5 else "collapse"
        pred_b = "survive" if prob_b > 0.5 else "collapse"
        pred_c = "survive" if prob_c > 0.5 else "collapse"
        
        # Input: feature summary
        input_data = {
            "project_id": project_id,
            "static_features": {
                "bus_factor": float(df_final.iloc[idx]["bus_factor"]),
                "contributor_count": float(df_final.iloc[idx]["contributor_count"]),
                "project_age": float(df_final.iloc[idx]["project_age"]),
                "stars": float(df_final.iloc[idx]["stars"]),
                "file_count": float(df_final.iloc[idx]["file_count"])
            },
            "fade_descriptors": {
                "slope": float(df_final.iloc[idx]["slope"]),
                "convexity": float(df_final.iloc[idx]["convexity"]),
                "decline_start": float(df_final.iloc[idx]["decline_start"]),
                "cliff_score": float(df_final.iloc[idx]["cliff_score"]),
                "is_plateau": float(df_final.iloc[idx]["is_plateau"]),
                "fade_idx": float(df_final.iloc[idx]["fade_idx"])
            }
        }
        
        # Output: true label
        output_data = {
            "survival": "survive" if true_label == 1 else "collapse",
            "post_departure_activity": float(df_final.iloc[idx]["post_departure_activity"])
        }
        
        example = {
            "input": json.dumps(input_data),
            "output": json.dumps(output_data),
            "metadata_fold": int(fold_a) if fold_a >= 0 else 0,
            "metadata_feature_names": ",".join(all_features),
            "predict_baseline_static": pred_a,
            "predict_fade_only": pred_b,
            "predict_combined": pred_c,
            "predict_baseline_static_prob": f"{prob_a:.4f}",
            "predict_fade_only_prob": f"{prob_b:.4f}",
            "predict_combined_prob": f"{prob_c:.4f}"
        }
        examples.append(example)
    
    # Build dataset structure for exp_gen_sol_out schema
    dataset_output = {
        "metadata": {
            "method_name": "founder_fade_curves_experiment",
            "description": "Testing Founder Fade Curves as Predictors of OSS Survival",
            "n_projects": len(df_final),
            "n_survived": int(np.sum(y_binary)),
            "n_collapsed": int(np.sum(1 - y_binary)),
            "cv_folds": 5,
            "metrics": {
                "model_a_auc": results["model_a_auc"],
                "model_a_auc_std": results["model_a_auc_std"],
                "model_b_auc": results["model_b_auc"],
                "model_b_auc_std": results["model_b_auc_std"],
                "model_c_auc": results["model_c_auc"],
                "model_c_auc_std": results["model_c_auc_std"],
                "model_a_r2": results["model_a_r2"],
                "model_b_r2": results["model_b_r2"],
                "model_c_r2": results["model_c_r2"],
                "model_d_r2": results["model_d_r2"]
            },
            "feature_importance": results["feature_importance"],
            "directionality": results["directionality"],
            "falsification_result": results["falsification_result"]
        },
        "datasets": [
            {
                "dataset": "oss_founder_fade_survival",
                "examples": examples
            }
        ]
    }
    
    return dataset_output


@logger.catch(reraise=True)
def main():
    logger.info("=" * 60)
    logger.info("Starting Founder Fade Curves Experiment")
    logger.info("=" * 60)
    
    # Load data
    df_static, df_ts = load_and_validate()
    
    # Run experiment
    output = run_experiment(df_static, df_ts)
    
    # Save output
    OUTPUT_PATH.write_text(json.dumps(output, indent=2))
    logger.info(f"Results saved to {OUTPUT_PATH}")
    logger.info("=" * 60)
    logger.info("Experiment completed successfully")
    logger.info("=" * 60)
    
    # Print summary
    print("\n" + "=" * 60)
    print("EXPERIMENT RESULTS SUMMARY")
    print("=" * 60)
    print(f"Total projects: {output['metadata']['n_projects']}")
    print(f"Survived: {output['metadata']['n_survived']}, Collapsed: {output['metadata']['n_collapsed']}")
    print(f"Model A (Static Only)    AUC: {output['metadata']['metrics']['model_a_auc']:.4f} ± {output['metadata']['metrics']['model_a_auc_std']:.4f}")
    print(f"Model B (Fade Only)      AUC: {output['metadata']['metrics']['model_b_auc']:.4f} ± {output['metadata']['metrics']['model_b_auc_std']:.4f}")
    print(f"Model C (Combined)       AUC: {output['metadata']['metrics']['model_c_auc']:.4f} ± {output['metadata']['metrics']['model_c_auc_std']:.4f}")
    print(f"Model D (Continuous)     R2:  {output['metadata']['metrics']['model_d_r2']:.4f}")
    print("-" * 60)
    print(f"Directionality: {output['metadata']['directionality']}")
    print(f"Falsification: {output['metadata']['falsification_result']}")
    print("=" * 60)


if __name__ == "__main__":
    main()