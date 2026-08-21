#!/usr/bin/env python3
"""
Founder Fade Curves as Predictors of OSS Survival Experiment

Compares temporal shape of founder involvement (smooth fade vs. abrupt cliff)
against static project metrics in predicting long-term project survival.
"""

from loguru import logger
from pathlib import Path
import json
import sys
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.model_selection import StratifiedKFold, KFold, cross_validate
from sklearn.inspection import permutation_importance
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, log_loss, r2_score
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")


def generate_synthetic_data(n_projects: int = 500, seed: int = 42) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Generate synthetic time-series and static data for OSS projects.
    
    Returns:
        df_static: DataFrame with project_id, bus_factor, contributor_count, 
                   project_age, stars, file_count, is_survived, post_departure_activity
        df_time_series: DataFrame with project_id, month_index, combined_share
    """
    np.random.seed(seed)
    
    project_ids = [f"proj_{i:04d}" for i in range(n_projects)]
    
    # Static features
    bus_factor = np.random.poisson(3, n_projects) + 1
    contributor_count = np.random.poisson(20, n_projects) + 1
    project_age = np.random.exponential(36, n_projects).astype(int) + 6
    stars = np.random.exponential(100, n_projects).astype(int) + 1
    file_count = np.random.poisson(50, n_projects) + 1
    
    # Time-series parameters
    n_months = np.random.randint(12, 48, n_projects)  # 1-4 years of data
    
    # Survival probability based on fade pattern
    survival_prob = []
    post_departure_activity = []
    
    time_series_data = []
    
    for i, pid in enumerate(project_ids):
        # Generate different fade patterns
        pattern_type = np.random.choice(['smooth', 'cliff', 'plateau_cliff', 'stable'], 
                                        p=[0.3, 0.3, 0.2, 0.2])
        
        months = np.arange(n_months[i])
        
        if pattern_type == 'smooth':
            # Smooth linear decline
            initial_share = np.random.uniform(0.5, 0.9)
            slope = np.random.uniform(-0.03, -0.01)
            noise = np.random.normal(0, 0.02, n_months[i])
            combined_share = np.clip(initial_share + slope * months + noise, 0, 1)
            survived = 1 if slope > -0.02 else 0
            post_dep = max(0, 1 + slope * 12)
            
        elif pattern_type == 'cliff':
            # Stable then sudden drop
            stable_months = n_months[i] - np.random.randint(2, 6)
            initial_share = np.random.uniform(0.5, 0.8)
            noise1 = np.random.normal(0, 0.01, stable_months)
            combined_share = np.clip(np.concatenate([
                np.full(stable_months, initial_share) + noise1,
                np.linspace(initial_share, np.random.uniform(0, 0.1), n_months[i] - stable_months) + 
                np.random.normal(0, 0.02, n_months[i] - stable_months)
            ]), 0, 1)
            survived = 0
            post_dep = np.random.uniform(0, 0.1)
            
        elif pattern_type == 'plateau_cliff':
            # Long plateau then cliff
            plateau_months = n_months[i] - np.random.randint(2, 8)
            initial_share = np.random.uniform(0.4, 0.7)
            noise1 = np.random.normal(0, 0.005, plateau_months)
            cliff_months = n_months[i] - plateau_months
            combined_share = np.clip(np.concatenate([
                np.full(plateau_months, initial_share) + noise1,
                np.linspace(initial_share, np.random.uniform(0, 0.05), cliff_months) +
                np.random.normal(0, 0.01, cliff_months)
            ]), 0, 1)
            survived = 0
            post_dep = np.random.uniform(0, 0.05)
            
        else:  # stable
            # Stable high involvement
            initial_share = np.random.uniform(0.6, 0.9)
            noise = np.random.normal(0, 0.015, n_months[i])
            combined_share = np.clip(initial_share + noise, 0, 1)
            survived = 1
            post_dep = initial_share + np.random.uniform(-0.1, 0.1)
        
        survival_prob.append(survived)
        post_departure_activity.append(np.clip(post_dep, 0, 1))
        
        for m, share in zip(months, combined_share):
            time_series_data.append({
                'project_id': pid,
                'month_index': m,
                'combined_share': share
            })
    
    df_static = pd.DataFrame({
        'project_id': project_ids,
        'bus_factor': bus_factor,
        'contributor_count': contributor_count,
        'project_age': project_age,
        'stars': stars,
        'file_count': file_count,
        'is_survived': survival_prob,
        'post_departure_activity': post_departure_activity
    })
    
    df_time_series = pd.DataFrame(time_series_data)
    
    logger.info(f"Generated {n_projects} projects with {len(df_time_series)} time-series records")
    logger.info(f"Survival rate: {np.mean(survival_prob):.2%}")
    
    return df_static, df_time_series


def compute_descriptors(group: pd.DataFrame) -> pd.Series:
    """Compute fade curve descriptors from a project's time-series."""
    t = group['month_index'].values
    y = group['combined_share'].values
    
    # Need at least 3 points for savgol
    if len(y) < 3:
        return pd.Series({
            'slope': 0.0, 'convexity': 0.0, 'decline_start': len(t),
            'cliff_score': 0.0, 'is_plateau': 0, 'fade_idx': 0.5
        })
    
    # Step A: Denoising with Savitzky-Golay
    window = min(5, len(y) // 2 * 2 - 1) or 3
    y_smooth = savgol_filter(y, window_length=window, polyorder=min(2, window - 1))
    
    # Descriptor 1: Linear Slope (S_slope)
    if len(t) > 1:
        slope, _ = np.polyfit(t, y_smooth, 1)
    else:
        slope = 0.0
    
    # Descriptor 2: Curvature/Convexity (S_convex)
    if len(y_smooth) >= 3:
        second_deriv = np.gradient(np.gradient(y_smooth))
        convexity = np.mean(second_deriv)
    else:
        convexity = 0.0
    
    # Descriptor 3: Time-to-Onset-of-Decline (S_decline_start)
    deriv = np.gradient(y_smooth)
    decline_indices = np.where(deriv < -0.01)[0]
    decline_start = int(decline_indices[0]) if len(decline_indices) > 0 else len(t)
    
    # Descriptor 4: Abrupt-Cliff Indicator (S_cliff)
    if len(y_smooth) > 8:
        recent_avg = np.mean(y_smooth[-8:-2])
        final_drop = recent_avg - np.mean(y_smooth[-2:])
        cliff_score = max(0, final_drop / (recent_avg + 1e-6))
    else:
        cliff_score = 0.0
    
    # Descriptor 5: Plateau-then-Cliff (S_plateau)
    is_plateau = 0
    if len(decline_indices) > 0 and len(y_smooth) > 10:
        idx = int(decline_indices[0])
        if idx > 5:
            plateau_variance = np.var(y_smooth[idx-5:idx])
            if plateau_variance < np.var(y_smooth) * 0.5:
                is_plateau = 1
    
    # Descriptor 6: Composite Fade Index (S_fade_idx)
    # 1.0 = perfect linear smooth decline, 0.0 = sudden drop
    fade_idx = np.clip(1.0 - cliff_score + (0.5 if slope < 0 else 0), 0, 1)
    
    return pd.Series({
        'slope': float(slope),
        'convexity': float(convexity),
        'decline_start': int(decline_start),
        'cliff_score': float(cliff_score),
        'is_plateau': int(is_plateau),
        'fade_idx': float(fade_idx)
    })


def run_experiment(df_static: pd.DataFrame, df_time_series: pd.DataFrame) -> dict:
    """Run the full experiment comparing baseline vs fade features."""
    
    # 3.1 Compute all descriptors
    logger.info("Computing fade curve descriptors...")
    features_fade = df_time_series.groupby('project_id').apply(compute_descriptors, include_groups=False).reset_index()
    df_final = df_static.merge(features_fade, on='project_id', how='left')
    
    # Fill any NaN from projects without time-series
    fade_cols = ['slope', 'convexity', 'decline_start', 'cliff_score', 'is_plateau', 'fade_idx']
    df_final[fade_cols] = df_final[fade_cols].fillna(0)
    
    # 3.2 Define Feature Sets
    X_static = df_final[['bus_factor', 'contributor_count', 'project_age', 'stars', 'file_count']].copy()
    X_fade = df_final[fade_cols].copy()
    X_combined = pd.concat([X_static, X_fade], axis=1)
    
    y_binary = df_final['is_survived'].values
    y_continuous = df_final['post_departure_activity'].values
    
    # Standardize features
    scaler_static = StandardScaler()
    scaler_fade = StandardScaler()
    scaler_combined = StandardScaler()
    
    X_static_scaled = scaler_static.fit_transform(X_static)
    X_fade_scaled = scaler_fade.fit_transform(X_fade)
    X_combined_scaled = scaler_combined.fit_transform(X_combined)
    
    # 3.3 Modeling Architecture
    cv_class = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_reg = KFold(n_splits=5, shuffle=True, random_state=42)
    
    models = {
        'model_a_static': LogisticRegression(penalty='l2', C=1.0, random_state=42, max_iter=1000, class_weight='balanced'),
        'model_b_fade': LogisticRegression(penalty='l2', C=1.0, random_state=42, max_iter=1000, class_weight='balanced'),
        'model_c_combined': LogisticRegression(penalty='l2', C=1.0, random_state=42, max_iter=1000, class_weight='balanced'),
    }
    
    reg_models = {
        'model_d_static': Ridge(alpha=1.0, random_state=42),
        'model_e_fade': Ridge(alpha=1.0, random_state=42),
        'model_f_combined': Ridge(alpha=1.0, random_state=42),
    }
    
    results = {}
    
    # Binary classification: survival prediction
    for name, model in models.items():
        if name == 'model_a_static':
            X = X_static_scaled
        elif name == 'model_b_fade':
            X = X_fade_scaled
        else:
            X = X_combined_scaled
        
        cv_results = cross_validate(
            model, X, y_binary, cv=cv_class,
            scoring=['roc_auc', 'neg_log_loss'],
            return_estimator=True,
            n_jobs=-1
        )
        
        results[name] = {
            'auc_mean': float(np.mean(cv_results['test_roc_auc'])),
            'auc_std': float(np.std(cv_results['test_roc_auc'])),
            'log_loss_mean': float(-np.mean(cv_results['test_neg_log_loss'])),
            'log_loss_std': float(np.std(cv_results['test_neg_log_loss'])),
        }
        logger.info(f"{name}: AUC={results[name]['auc_mean']:.4f}±{results[name]['auc_std']:.4f}, "
                   f"LogLoss={results[name]['log_loss_mean']:.4f}±{results[name]['log_loss_std']:.4f}")
    
    # Continuous regression: post-departure activity
    for name, model in reg_models.items():
        if name == 'model_d_static':
            X = X_static_scaled
        elif name == 'model_e_fade':
            X = X_fade_scaled
        else:
            X = X_combined_scaled
        
        cv_results = cross_validate(
            model, X, y_continuous, cv=cv_reg,
            scoring=['r2', 'neg_mean_squared_error'],
            return_estimator=True,
            n_jobs=-1
        )
        
        results[name] = {
            'r2_mean': float(np.mean(cv_results['test_r2'])),
            'r2_std': float(np.std(cv_results['test_r2'])),
            'mse_mean': float(-np.mean(cv_results['test_neg_mean_squared_error'])),
            'mse_std': float(np.std(cv_results['test_neg_mean_squared_error'])),
        }
        logger.info(f"{name}: R²={results[name]['r2_mean']:.4f}±{results[name]['r2_std']:.4f}, "
                   f"MSE={results[name]['mse_mean']:.4f}±{results[name]['mse_std']:.4f}")
    
    # 3.5 Falsification Control: Use a non-founder user's fade descriptors
    logger.info("Running falsification control...")
    # Simulate by shuffling fade features across projects
    X_fade_shuffled = X_fade_scaled.copy()
    np.random.shuffle(X_fade_shuffled)
    
    falsification_model = LogisticRegression(penalty='l2', C=1.0, random_state=42, max_iter=1000, class_weight='balanced')
    cv_fals = cross_validate(falsification_model, X_fade_shuffled, y_binary, cv=cv_class, scoring=['roc_auc'])
    falsification_auc = float(np.mean(cv_fals['test_roc_auc']))
    
    results['falsification'] = {
        'shuffled_fade_auc': falsification_auc,
        'significant_difference': results['model_b_fade']['auc_mean'] > falsification_auc + 0.02
    }
    
    # 3.6 Feature Importance on Combined Model
    logger.info("Computing feature importance...")
    combined_model = LogisticRegression(penalty='l2', C=1.0, random_state=42, max_iter=1000, class_weight='balanced')
    combined_model.fit(X_combined_scaled, y_binary)
    
    perm_importance = permutation_importance(combined_model, X_combined_scaled, y_binary, 
                                              n_repeats=30, random_state=42, n_jobs=-1)
    
    feature_names = list(X_combined.columns)
    importance_dict = dict(zip(feature_names, perm_importance.importances_mean.tolist()))
    
    fade_importance = {k: v for k, v in importance_dict.items() if k in fade_cols}
    static_importance = {k: v for k, v in importance_dict.items() if k in X_static.columns}
    
    # Directionality
    fade_idx_corr = np.corrcoef(df_final['fade_idx'], df_final['is_survived'])[0, 1]
    directionality = 'Positive' if fade_idx_corr > 0 else 'Negative'
    
    return {
        'metrics': results,
        'feature_importance': {
            'fade_descriptors': fade_importance,
            'static_descriptors': static_importance
        },
        'directionality': f'{directionality} correlation between fade_idx and survival (r={fade_idx_corr:.3f})',
        'falsification_result': 'Significant difference in AUC' if results['falsification']['significant_difference'] 
                                 else 'No significant difference in AUC',
        'n_projects': len(df_final),
        'n_features_static': len(X_static.columns),
        'n_features_fade': len(X_fade.columns)
    }


def main():
    """Main experiment entry point."""
    logger.info("Starting Founder Fade Curves experiment")
    
    # Generate synthetic data
    df_static, df_time_series = generate_synthetic_data(n_projects=500, seed=42)
    
    # Run experiment
    results = run_experiment(df_static, df_time_series)
    
    # Prepare output in exp_gen_sol_out format
    output = {
        "metadata": {
            "method_name": "Founder_Fade_Curves_Experiment",
            "description": "Comparative study evaluating whether temporal shape of founder involvement predicts OSS survival",
            "n_projects": results['n_projects'],
            "n_static_features": results['n_features_static'],
            "n_fade_features": results['n_features_fade']
        },
        "datasets": [{
            "dataset": "synthetic_oss_survival",
            "examples": []
        }]
    }
    
    # Add per-example predictions for each model
    # Re-run to get per-fold predictions
    features_fade = df_time_series.groupby('project_id').apply(compute_descriptors, include_groups=False).reset_index()
    df_final = df_static.merge(features_fade, on='project_id', how='left')
    fade_cols = ['slope', 'convexity', 'decline_start', 'cliff_score', 'is_plateau', 'fade_idx']
    df_final[fade_cols] = df_final[fade_cols].fillna(0)
    
    X_static = df_final[['bus_factor', 'contributor_count', 'project_age', 'stars', 'file_count']]
    X_fade = df_final[fade_cols]
    X_combined = pd.concat([X_static, X_fade], axis=1)
    
    y_binary = df_final['is_survived'].values
    
    scaler_combined = StandardScaler()
    X_combined_scaled = scaler_combined.fit_transform(X_combined)
    
    # Train final models on all data for predictions
    model_static = LogisticRegression(penalty='l2', C=1.0, random_state=42, max_iter=1000, class_weight='balanced')
    model_fade = LogisticRegression(penalty='l2', C=1.0, random_state=42, max_iter=1000, class_weight='balanced')
    model_combined = LogisticRegression(penalty='l2', C=1.0, random_state=42, max_iter=1000, class_weight='balanced')
    
    scaler_static = StandardScaler()
    scaler_fade = StandardScaler()
    X_static_scaled = scaler_static.fit_transform(X_static)
    X_fade_scaled = scaler_fade.fit_transform(X_fade)
    
    model_static.fit(X_static_scaled, y_binary)
    model_fade.fit(X_fade_scaled, y_binary)
    model_combined.fit(X_combined_scaled, y_binary)
    
    pred_static = model_static.predict_proba(X_static_scaled)[:, 1]
    pred_fade = model_fade.predict_proba(X_fade_scaled)[:, 1]
    pred_combined = model_combined.predict_proba(X_combined_scaled)[:, 1]
    
    # Build examples
    examples = []
    for i in range(len(df_final)):
        examples.append({
            "input": f"Project {df_final.iloc[i]['project_id']}: bus_factor={df_final.iloc[i]['bus_factor']}, "
                     f"contributors={df_final.iloc[i]['contributor_count']}, age={df_final.iloc[i]['project_age']}mo, "
                     f"stars={df_final.iloc[i]['stars']}, files={df_final.iloc[i]['file_count']}, "
                     f"fade_slope={df_final.iloc[i]['slope']:.4f}, fade_convexity={df_final.iloc[i]['convexity']:.4f}, "
                     f"fade_decline_start={df_final.iloc[i]['decline_start']}, fade_cliff={df_final.iloc[i]['cliff_score']:.4f}, "
                     f"fade_plateau={df_final.iloc[i]['is_plateau']}, fade_idx={df_final.iloc[i]['fade_idx']:.4f}",
            "output": str(int(y_binary[i])),
            "metadata_project_id": df_final.iloc[i]['project_id'],
            "metadata_fold": 0,
            "predict_static_only": f"{pred_static[i]:.4f}",
            "predict_fade_only": f"{pred_fade[i]:.4f}",
            "predict_combined": f"{pred_combined[i]:.4f}"
        })
    
    output["datasets"][0]["examples"] = examples
    
    # Save full output
    output_path = Path("method_out.json")
    output_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Saved full output to {output_path}")
    
    # Also save a summary results file for quick inspection
    summary = {
        "title": "Founder Fade Curves as Predictors of OSS Survival",
        "metrics": results['metrics'],
        "feature_importance": results['feature_importance'],
        "directionality": results['directionality'],
        "falsification_result": results['falsification_result'],
        "n_projects": results['n_projects']
    }
    Path("results_summary.json").write_text(json.dumps(summary, indent=2))
    logger.info("Saved summary to results_summary.json")
    
    return output


if __name__ == "__main__":
    main()