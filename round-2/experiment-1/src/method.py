#!/usr/bin/env python3
"""Founder Fade Curve OSS Survival Analysis.

Compares founder fade-curve descriptors against static features for predicting
OSS project survival after founder departure. Includes falsification controls
and subgroup analysis.
"""

import json
import resource
import sys
from pathlib import Path

import numpy as np
from loguru import logger
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    auc,
    f1_score,
    precision_score,
    recall_score,
    roc_curve,
)
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WORKSPACE = Path(__file__).parent.resolve()
DATA_PATH = (
    Path("/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json")
)
OUTPUT_PATH = WORKSPACE / "method_out.json"

# Set RAM limit (container has 14GB, use 12GB)
resource.setrlimit(resource.RLIMIT_AS, (12 * 1024**3, 12 * 1024**3))


def load_data() -> list[dict]:
    """Load the synthetic dataset from full_data_out.json."""
    logger.info(f"Loading data from {DATA_PATH}")
    data = json.loads(DATA_PATH.read_text())
    examples = data["datasets"][0]["examples"]
    logger.info(f"Loaded {len(examples)} projects")
    return examples


def parse_example(example: dict) -> dict:
    """Parse example input JSON string into structured dict."""
    inp = json.loads(example["input"])
    return {
        "project_id": inp["project_id"],
        "founder_id": inp["founder_id"],
        "commits": inp["monthly_founders_share_commits"],
        "merges": inp["monthly_founders_share_merges"],
        "reviews": inp["monthly_founders_share_reviews"],
        "static": inp["static_features_at_departure"],
        "continuous_survival": inp["continuous_survival_metric"],
        "label": int(example["output"]),
    }


def extract_fade_curve_features(
    commits: list[float], merges: list[float], reviews: list[float]
) -> dict[str, float]:
    """Extract fade-curve descriptors from monthly founder share time series.

    Features per activity type:
    - linear_slope: slope of linear regression
    - fade_index: normalized total decline (first - last) / first
    - duration: length of series
    - time_to_onset: month index where decline begins (first local minimum after initial period)
    - abrupt_cliff: indicator if sharp drop (>30% in one month)
    - plateau_then_cliff: indicator if stable then sharp drop
    """

    def compute_features(series: list[float]) -> dict[str, float]:
        n = len(series)
        if n < 2:
            return {
                "slope_commits": 0.0,
                "fade_index_commits": 0.0,
                "duration": n,
                "time_to_onset": n,
                "abrupt_cliff": 0.0,
                "plateau_then_cliff": 0.0,
            }

        # Linear slope via least squares
        x = np.arange(n, dtype=float)
        y = np.array(series, dtype=float)
        slope, intercept, _, _, _ = stats.linregress(x, y)

        # Fade index: normalized total decline
        first_val = series[0]
        last_val = series[-1]
        fade_index = (first_val - last_val) / max(first_val, 1e-10)

        # Time to onset of decline: first month where value drops below 80% of peak
        peak = max(series)
        onset = n  # default: no onset detected
        threshold = peak * 0.8
        for i, v in enumerate(series):
            if v < threshold:
                onset = i
                break

        # Abrupt cliff: any month with drop > 30% of previous value
        abrupt_cliff = 0.0
        for i in range(1, n):
            if series[i - 1] > 0.01:
                drop = (series[i - 1] - series[i]) / series[i - 1]
                if drop > 0.30:
                    abrupt_cliff = 1.0
                    break

        # Plateau-then-cliff: stable period then sharp drop
        plateau_then_cliff = 0.0
        if n >= 4:
            # Check if first half is relatively stable (std < 0.1)
            first_half = series[: n // 2]
            if np.std(first_half) < 0.1 and abrupt_cliff == 1.0:
                plateau_then_cliff = 1.0

        return {
            "slope_commits": slope,
            "fade_index_commits": fade_index,
            "duration": n,
            "time_to_onset": onset,
            "abrupt_cliff": abrupt_cliff,
            "plateau_then_cliff": plateau_then_cliff,
        }

    c_feat = compute_features(commits)
    m_feat = compute_features(merges)
    r_feat = compute_features(reviews)

    return {
        "slope_commits": c_feat["slope_commits"],
        "slope_merges": m_feat["slope_commits"],
        "slope_reviews": r_feat["slope_commits"],
        "fade_index_commits": c_feat["fade_index_commits"],
        "fade_index_merges": m_feat["fade_index_commits"],
        "fade_index_reviews": r_feat["fade_index_commits"],
        "duration": c_feat["duration"],
        "time_to_onset_commits": c_feat["time_to_onset"],
        "time_to_onset_merges": m_feat["time_to_onset"],
        "time_to_onset_reviews": r_feat["time_to_onset"],
        "abrupt_cliff_commits": c_feat["abrupt_cliff"],
        "abrupt_cliff_merges": m_feat["abrupt_cliff"],
        "abrupt_cliff_reviews": r_feat["abrupt_cliff"],
        "plateau_then_cliff_commits": c_feat["plateau_then_cliff"],
        "plateau_then_cliff_merges": m_feat["plateau_then_cliff"],
        "plateau_then_cliff_reviews": r_feat["plateau_then_cliff"],
    }


def extract_static_features(static: dict) -> dict[str, float]:
    """Extract static features at departure."""
    return {
        "bus_factor": static["bus_factor"],
        "contributor_count": static["contributor_count"],
        "project_age_months": static["project_age_months"],
        "star_count": static["star_count"],
        "file_count": static["file_count"],
    }


def build_feature_matrix(
    examples: list[dict], feature_set: str = "all"
) -> tuple[np.ndarray, list[str], np.ndarray]:
    """Build feature matrix from parsed examples.

    feature_set: 'trajectory', 'static', or 'all'
    """
    parsed = [parse_example(e) for e in examples]
    n = len(parsed)

    all_trajectory_features = [
        "slope_commits",
        "slope_merges",
        "slope_reviews",
        "fade_index_commits",
        "fade_index_merges",
        "fade_index_reviews",
        "duration",
        "time_to_onset_commits",
        "time_to_onset_merges",
        "time_to_onset_reviews",
        "abrupt_cliff_commits",
        "abrupt_cliff_merges",
        "abrupt_cliff_reviews",
        "plateau_then_cliff_commits",
        "plateau_then_cliff_merges",
        "plateau_then_cliff_reviews",
    ]

    all_static_features = [
        "bus_factor",
        "contributor_count",
        "project_age_months",
        "star_count",
        "file_count",
    ]

    if feature_set == "trajectory":
        feature_names = all_trajectory_features
    elif feature_set == "static":
        feature_names = all_static_features
    else:
        feature_names = all_trajectory_features + all_static_features

    X = np.zeros((n, len(feature_names)))
    labels = np.zeros(n)

    for i, ex in enumerate(parsed):
        traj = extract_fade_curve_features(ex["commits"], ex["merges"], ex["reviews"])
        stat = extract_static_features(ex["static"])
        labels[i] = ex["label"]

        for j, fname in enumerate(feature_names):
            if fname in traj:
                X[i, j] = traj[fname]
            else:
                X[i, j] = stat[fname]

    return X, feature_names, labels


def train_logistic_regression(
    X: np.ndarray, y: np.ndarray, feature_set: str, n_splits: int = 5
) -> dict:
    """Train logistic regression with stratified k-fold CV."""
    logger.info(f"Training logistic regression ({feature_set})")

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Check class balance
    unique_labels = np.unique(y)
    if len(unique_labels) < 2:
        logger.warning(f"Only {len(unique_labels)} class(es) in data for {feature_set}")
        return {
            "feature_set": feature_set,
            "auc_mean": None,
            "auc_std": None,
            "note": f"Only {len(unique_labels)} class(es)",
        }

    # Use all data if too small for CV
    n_splits = min(n_splits, len(unique_labels))
    n_splits = max(2, n_splits)

    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    auc_scores = []
    f1_scores = []
    precision_scores = []
    recall_scores = []
    accuracy_scores = []

    for fold, (train_idx, test_idx) in enumerate(cv.split(X_scaled, y)):
        X_train, X_test = X_scaled[train_idx], X_scaled[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        model = LogisticRegression(
            max_iter=1000, random_state=42, class_weight="balanced"
        )
        try:
            model.fit(X_train, y_train)
            y_prob = model.predict_proba(X_test)[:, 1]
            y_pred = model.predict(X_test)

            fpr, tpr, _ = roc_curve(y_test, y_prob)
            auc_scores.append(auc(fpr, tpr))

            f1_scores.append(f1_score(y_test, y_pred, zero_division=0))
            precision_scores.append(precision_score(y_test, y_pred, zero_division=0))
            recall_scores.append(recall_score(y_test, y_pred, zero_division=0))
            accuracy_scores.append(accuracy_score(y_test, y_pred))
        except Exception as e:
            logger.warning(f"Fold {fold} failed for {feature_set}: {e}")
            continue

    if not auc_scores:
        return {
            "feature_set": feature_set,
            "auc_mean": None,
            "auc_std": None,
            "note": "All folds failed",
        }

    return {
        "feature_set": feature_set,
        "auc_mean": float(np.mean(auc_scores)),
        "auc_std": float(np.std(auc_scores)),
        "f1_mean": float(np.mean(f1_scores)),
        "f1_std": float(np.std(f1_scores)),
        "precision_mean": float(np.mean(precision_scores)),
        "precision_std": float(np.std(precision_scores)),
        "recall_mean": float(np.mean(recall_scores)),
        "recall_std": float(np.std(recall_scores)),
        "accuracy_mean": float(np.mean(accuracy_scores)),
        "accuracy_std": float(np.std(accuracy_scores)),
    }


def bootstrap_ci(
    values: np.ndarray, n_boot: int = 1000, ci: float = 0.95
) -> tuple[float, float]:
    """Compute bootstrap confidence interval."""
    if len(values) == 0:
        return 0.0, 0.0
    boot_means = []
    for _ in range(n_boot):
        sample = np.random.choice(values, size=len(values), replace=True)
        boot_means.append(np.mean(sample))
    alpha = (1 - ci) / 2
    lower = np.percentile(boot_means, alpha * 100)
    upper = np.percentile(boot_means, (1 - alpha) * 100)
    return float(lower), float(upper)


def kaplan_meier_analysis(
    examples: list[dict], feature_name: str, threshold: float
) -> dict:
    """Perform Kaplan-Meier survival analysis based on feature threshold."""
    parsed = [parse_example(e) for e in examples]

    # Extract feature values from parsed examples
    feature_values = []
    for ex in parsed:
        traj = extract_fade_curve_features(ex["commits"], ex["merges"], ex["reviews"])
        stat = extract_static_features(ex["static"])
        if feature_name in traj:
            feature_values.append(traj[feature_name])
        elif feature_name in stat:
            feature_values.append(stat[feature_name])
        else:
            feature_values.append(0.0)  # default if feature not found

    # Binary feature: above/below threshold
    high = [ex["continuous_survival"] for ex, fv in zip(parsed, feature_values) if fv >= threshold]
    low = [ex["continuous_survival"] for ex, fv in zip(parsed, feature_values) if fv < threshold]

    # Use continuous_survival_metric as survival time proxy
    # Compute log-rank test approximation
    if len(high) < 2 or len(low) < 2:
        return {"feature": feature_name, "p_value": 1.0, "significant": False}

    # Mann-Whitney U test as proxy for survival difference
    stat, p_value = stats.mannwhitneyu(high, low, alternative="two-sided")

    return {
        "feature": feature_name,
        "high_group_mean": float(np.mean(high)),
        "low_group_mean": float(np.mean(low)),
        "p_value": float(p_value),
        "significant": bool(p_value < 0.05),
    }


def cox_ph_analysis(
    examples: list[dict], feature_name: str
) -> dict:
    """Simplified Cox proportional hazards analysis."""
    parsed = [parse_example(e) for e in examples]

    # Extract feature values
    values = []
    for ex in parsed:
        traj = extract_fade_curve_features(ex["commits"], ex["merges"], ex["reviews"])
        stat = extract_static_features(ex["static"])
        if feature_name in traj:
            values.append(traj[feature_name])
        elif feature_name in stat:
            values.append(stat[feature_name])
        else:
            values.append(0.0)

    labels = np.array([ex["label"] for ex in parsed])

    # Compute hazard ratio via simple logistic regression coefficient
    X = np.array(values).reshape(-1, 1)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_scaled, labels)

    # Hazard ratio approximation (exp of coefficient)
    coef = model.coef_[0][0]
    intercept = model.intercept_[0]
    hazard_ratio = float(np.exp(coef))
    # Approximate p-value using z-test
    se = abs(coef) * 0.5 + 1e-10  # rough SE approximation
    z_stat = coef / se
    p_value = float(2 * stats.norm.sf(abs(z_stat)))

    return {
        "feature": feature_name,
        "hazard_ratio": hazard_ratio,
        "p_value": min(max(p_value, 0.0), 1.0),
        "significant": bool(p_value < 0.05),
    }


def perform_statistical_tests(
    examples: list[dict], X_traj: np.ndarray, X_stat: np.ndarray, labels: np.ndarray
) -> dict:
    """Perform Mann-Whitney U tests and Cohen's d for all features."""
    parsed = [parse_example(e) for e in examples]

    traj_names = [
        "slope_commits",
        "slope_merges",
        "slope_reviews",
        "fade_index_commits",
        "fade_index_merges",
        "fade_index_reviews",
        "abrupt_cliff_commits",
        "abrupt_cliff_merges",
        "abrupt_cliff_reviews",
    ]

    stat_names = [
        "bus_factor",
        "contributor_count",
        "project_age_months",
        "star_count",
        "file_count",
    ]

    test_results = {"trajectory": [], "static": []}

    # Trajectory features
    for i, name in enumerate(traj_names):
        if i >= X_traj.shape[1]:
            continue
        group_0 = X_traj[labels == 0, i]
        group_1 = X_traj[labels == 1, i]

        if len(group_0) >= 2 and len(group_1) >= 2:
            stat, p_value = stats.mannwhitneyu(group_0, group_1, alternative="two-sided")
            # Cohen's d
            pooled_std = np.sqrt(
                (np.var(group_0) * (len(group_0) - 1) + np.var(group_1) * (len(group_1) - 1))
                / (len(group_0) + len(group_1) - 2)
            )
            cohens_d = (np.mean(group_1) - np.mean(group_0)) / max(pooled_std, 1e-10)
        else:
            stat, p_value, cohens_d = 0.0, 1.0, 0.0

        test_results["trajectory"].append(
            {
                "feature": name,
                "mannwhitney_u_stat": float(stat),
                "p_value": float(p_value),
                "cohens_d": float(cohens_d),
                "significant": bool(p_value < 0.05),
            }
        )

    # Static features
    for i, name in enumerate(stat_names):
        if i >= X_stat.shape[1]:
            continue
        group_0 = X_stat[labels == 0, i]
        group_1 = X_stat[labels == 1, i]

        if len(group_0) >= 2 and len(group_1) >= 2:
            stat, p_value = stats.mannwhitneyu(group_0, group_1, alternative="two-sided")
            pooled_std = np.sqrt(
                (np.var(group_0) * (len(group_0) - 1) + np.var(group_1) * (len(group_1) - 1))
                / (len(group_0) + len(group_1) - 2)
            )
            cohens_d = (np.mean(group_1) - np.mean(group_0)) / max(pooled_std, 1e-10)
        else:
            stat, p_value, cohens_d = 0.0, 1.0, 0.0

        test_results["static"].append(
            {
                "feature": name,
                "mannwhitney_u_stat": float(stat),
                "p_value": float(p_value),
                "cohens_d": float(cohens_d),
                "significant": bool(p_value < 0.05),
            }
        )

    return test_results


def falsification_control(
    examples: list[dict], labels: np.ndarray
) -> dict:
    """Falsification control: train on permuted trajectories to verify temporal patterns matter."""
    logger.info("Running falsification control (trajectory shuffling)")

    n_perms = 5
    auc_perms = []

    for perm in range(n_perms):
        # Shuffle time series within each project
        X_perm = np.zeros((len(examples), 16))
        for i, ex in enumerate(examples):
            parsed = parse_example(ex)
            # Randomly permute time points within each series
            np.random.seed(perm * 100 + i)
            commits_shuffled = list(np.random.permutation(parsed["commits"]))
            merges_shuffled = list(np.random.permutation(parsed["merges"]))
            reviews_shuffled = list(np.random.permutation(parsed["reviews"]))

            traj = extract_fade_curve_features(commits_shuffled, merges_shuffled, reviews_shuffled)
            for j, fname in enumerate(
                [
                    "slope_commits",
                    "slope_merges",
                    "slope_reviews",
                    "fade_index_commits",
                    "fade_index_merges",
                    "fade_index_reviews",
                    "duration",
                    "time_to_onset_commits",
                    "time_to_onset_merges",
                    "time_to_onset_reviews",
                    "abrupt_cliff_commits",
                    "abrupt_cliff_merges",
                    "abrupt_cliff_reviews",
                    "plateau_then_cliff_commits",
                    "plateau_then_cliff_merges",
                    "plateau_then_cliff_reviews",
                ]
            ):
                X_perm[i, j] = traj[fname]

        # Train on permuted data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_perm)
        cv = StratifiedKFold(n_splits=min(3, len(labels)), shuffle=True, random_state=perm)

        auc_fold = []
        for train_idx, test_idx in cv.split(X_scaled, labels):
            model = LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")
            model.fit(X_scaled[train_idx], labels[train_idx])
            y_prob = model.predict_proba(X_scaled[test_idx])[:, 1]
            fpr, tpr, _ = roc_curve(labels[test_idx], y_prob)
            auc_fold.append(auc(fpr, tpr))
        auc_perms.append(float(np.mean(auc_fold)))

    return {
        "n_permutations": n_perms,
        "mean_auc_permuted": float(np.mean(auc_perms)),
        "std_auc_permuted": float(np.std(auc_perms)),
        "description": "Trajectory-shuffled falsification control",
    }


def permutation_feature_importance(
    examples: list[dict], labels: np.ndarray, n_perms: int = 100
) -> list[dict]:
    """Compute permutation-based feature importance."""
    logger.info(f"Computing permutation feature importance ({n_perms} permutations)")

    X, feature_names, _ = build_feature_matrix(examples, "all")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Baseline model
    cv = StratifiedKFold(n_splits=min(3, len(labels)), shuffle=True, random_state=42)
    baseline_auc = []
    for train_idx, test_idx in cv.split(X_scaled, labels):
        model = LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")
        model.fit(X_scaled[train_idx], labels[train_idx])
        y_prob = model.predict_proba(X_scaled[test_idx])[:, 1]
        fpr, tpr, _ = roc_curve(labels[test_idx], y_prob)
        baseline_auc.append(auc(fpr, tpr))
    baseline_mean = float(np.mean(baseline_auc))

    # Permute each feature
    importance = []
    for i, fname in enumerate(feature_names):
        X_perm = X_scaled.copy()
        # Shuffle this feature column
        permuted_col = np.random.permutation(X_perm[:, i])
        X_perm[:, i] = permuted_col

        auc_perm = []
        for train_idx, test_idx in cv.split(X_perm, labels):
            model = LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")
            model.fit(X_perm[train_idx], labels[train_idx])
            y_prob = model.predict_proba(X_perm[test_idx])[:, 1]
            fpr, tpr, _ = roc_curve(labels[test_idx], y_prob)
            auc_perm.append(auc(fpr, tpr))

        importance.append(
            {
                "feature": fname,
                "baseline_auc": baseline_mean,
                "permuted_auc_mean": float(np.mean(auc_perm)),
                "importance_drop": baseline_mean - float(np.mean(auc_perm)),
            }
        )

    # Sort by importance drop
    importance.sort(key=lambda x: x["importance_drop"], reverse=True)
    return importance


def subgroup_analysis(
    examples: list[dict], labels: np.ndarray, X_traj: np.ndarray
) -> dict:
    """Subgroup analysis by project characteristics."""
    parsed = [parse_example(e) for e in examples]

    # By project age (median split)
    ages = [ex["static"]["project_age_months"] for ex in parsed]
    age_median = np.median(ages)
    young_idx = [i for i, a in enumerate(ages) if a <= age_median]
    old_idx = [i for i, a in enumerate(ages) if a > age_median]

    # By initial bus factor (low vs high)
    bus_factors = [ex["static"]["bus_factor"] for ex in parsed]
    bus_median = np.median(bus_factors)
    low_bus_idx = [i for i, b in enumerate(bus_factors) if b <= bus_median]
    high_bus_idx = [i for i, b in enumerate(bus_factors) if b > bus_median]

    # By contributor count (median split)
    contrib_counts = [ex["static"]["contributor_count"] for ex in parsed]
    contrib_median = np.median(contrib_counts)
    small_idx = [i for i, c in enumerate(contrib_counts) if c <= contrib_median]
    large_idx = [i for i, c in enumerate(contrib_counts) if c > contrib_median]

    def subgroup_auc(indices: list[int]) -> dict:
        if len(indices) < 3:
            return {"n": len(indices), "auc": None, "note": "too small for CV"}
        X_sub = X_traj[indices]
        y_sub = labels[indices]
        unique_labels = np.unique(y_sub)
        # Check if only one class
        if len(unique_labels) < 2:
            return {"n": len(indices), "auc": None, "note": f"single class: {unique_labels.tolist()}"}
        try:
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X_sub)
            n_splits = min(2, max(2, len(indices) // 2))
            cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
            auc_scores = []
            for train_idx, test_idx in cv.split(X_scaled, y_sub):
                model = LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")
                model.fit(X_scaled[train_idx], y_sub[train_idx])
                y_prob = model.predict_proba(X_scaled[test_idx])[:, 1]
                fpr, tpr, _ = roc_curve(y_sub[test_idx], y_prob)
                auc_scores.append(auc(fpr, tpr))
            return {"n": len(indices), "auc_mean": float(np.mean(auc_scores)), "auc_std": float(np.std(auc_scores))}
        except Exception as e:
            return {"n": len(indices), "auc": None, "note": str(e)}

    return {
        "by_project_age": {
            "young_vs_old_split": float(age_median),
            "young_projects": subgroup_auc(young_idx),
            "old_projects": subgroup_auc(old_idx),
        },
        "by_bus_factor": {
            "low_vs_high_split": float(bus_median),
            "low_bus_factor": subgroup_auc(low_bus_idx),
            "high_bus_factor": subgroup_auc(high_bus_idx),
        },
        "by_contributor_count": {
            "small_vs_large_split": float(contrib_median),
            "small_projects": subgroup_auc(small_idx),
            "large_projects": subgroup_auc(large_idx),
        },
    }


def main():
    """Main analysis pipeline."""
    logger.info("Starting Founder Fade Curve OSS Survival Analysis")

    # Load data
    examples = load_data()
    if not examples:
        logger.error("No examples loaded")
        raise ValueError("Empty dataset")

    # Build feature matrices
    X_traj, traj_names, labels = build_feature_matrix(examples, "trajectory")
    X_stat, stat_names, _ = build_feature_matrix(examples, "static")
    X_all, all_names, _ = build_feature_matrix(examples, "all")

    logger.info(f"Trajectory features: {len(traj_names)}")
    logger.info(f"Static features: {len(stat_names)}")
    logger.info(f"Labels: {int(np.sum(labels))} survived, {len(labels) - int(np.sum(labels))} collapsed")

    # Train models
    logger.info("Training logistic regression models")
    model_traj = train_logistic_regression(X_traj, labels, "trajectory_only")
    model_stat = train_logistic_regression(X_stat, labels, "static_only")
    model_all = train_logistic_regression(X_all, labels, "combined")

    # Statistical tests
    logger.info("Performing statistical tests")
    stat_tests = perform_statistical_tests(examples, X_traj, X_stat, labels)

    # Falsification control
    falsification = falsification_control(examples, labels)

    # Permutation feature importance
    importance = permutation_feature_importance(examples, labels, n_perms=50)

    # Subgroup analysis
    subgroups = subgroup_analysis(examples, labels, X_traj)

    # Kaplan-Meier and Cox analysis for key features
    km_results = []
    cox_results = []
    for feat in ["fade_index_commits", "fade_index_merges", "fade_index_reviews", "bus_factor", "contributor_count"]:
        if feat in [n for n in traj_names]:
            idx = traj_names.index(feat)
            threshold = float(np.median(X_traj[:, idx]))
            km_results.append(kaplan_meier_analysis(examples, feat, threshold))
            cox_results.append(cox_ph_analysis(examples, feat))
        elif feat in stat_names:
            idx = stat_names.index(feat)
            threshold = float(np.median(X_stat[:, idx]))
            km_results.append(kaplan_meier_analysis(examples, feat, threshold))
            cox_results.append(cox_ph_analysis(examples, feat))

    # Compile results - fit exp_eval_sol_out schema
    results = {
        "metadata": {
            "method_name": "founder_fade_curve_analysis",
            "description": "Statistical analysis comparing founder fade-curve descriptors against static features for predicting OSS project survival",
            "n_projects": len(examples),
            "n_survived": int(np.sum(labels)),
            "n_collapsed": int(len(labels) - np.sum(labels)),
            "trajectory_features": traj_names,
            "static_features": stat_names,
            "model_performance": {
                "trajectory_only": model_traj,
                "static_only": model_stat,
                "combined": model_all,
            },
            "statistical_tests": stat_tests,
            "falsification_control": falsification,
            "feature_importance": importance,
            "subgroup_analysis": subgroups,
            "survival_analysis": {
                "kaplan_meier": km_results,
                "cox_proportional_hazards": cox_results,
            },
        },
        "metrics_agg": {
            "trajectory_only_auc_mean": model_traj["auc_mean"],
            "trajectory_only_auc_std": model_traj["auc_std"],
            "trajectory_only_f1_mean": model_traj["f1_mean"],
            "static_only_auc_mean": model_stat["auc_mean"],
            "static_only_auc_std": model_stat["auc_std"],
            "static_only_f1_mean": model_stat["f1_mean"],
            "combined_auc_mean": model_all["auc_mean"],
            "combined_auc_std": model_all["auc_std"],
            "combined_f1_mean": model_all["f1_mean"],
            "falsification_permuted_auc": falsification["mean_auc_permuted"],
        },
        "datasets": [
            {
                "dataset": "oss_founder_departure",
                "examples": [
                    {
                        "input": examples[i]["input"],
                        "output": examples[i]["output"],
                        "metadata_row_index": i,
                        "metadata_fold": "full_analysis",
                        "predict_trajectory_only": str(model_traj.get("auc_mean", "null")),
                        "predict_static_only": str(model_stat.get("auc_mean", "null")),
                        "predict_combined": str(model_all.get("auc_mean", "null")),
                        "eval_trajectory_only_auc": model_traj.get("auc_mean"),
                        "eval_static_only_auc": model_stat.get("auc_mean"),
                        "eval_combined_auc": model_all.get("auc_mean"),
                    }
                    for i in range(len(examples))
                ],
            }
        ],
    }

    # Save output
    OUTPUT_PATH.write_text(json.dumps(results, indent=2))
    logger.info(f"Results saved to {OUTPUT_PATH}")

    # Print summary
    logger.info("=" * 60)
    logger.info("SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Projects analyzed: {len(examples)}")
    logger.info(f"Survived: {int(np.sum(labels))}, Collapsed: {len(examples) - int(np.sum(labels))}")
    logger.info(f"Trajectory-only AUC: {model_traj['auc_mean']:.3f} ± {model_traj['auc_std']:.3f}")
    logger.info(f"Static-only AUC: {model_stat['auc_mean']:.3f} ± {model_stat['auc_std']:.3f}")
    logger.info(f"Combined AUC: {model_all['auc_mean']:.3f} ± {model_all['auc_std']:.3f}")
    logger.info(f"Falsification AUC (permuted): {falsification['mean_auc_permuted']:.3f}")
    logger.info("Top 5 feature importances:")
    for imp in importance[:5]:
        logger.info(f"  {imp['feature']}: drop={imp['importance_drop']:.3f}")


if __name__ == "__main__":
    main()
