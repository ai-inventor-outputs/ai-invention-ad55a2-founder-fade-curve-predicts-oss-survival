#!/usr/bin/env python3
"""Generate synthetic OSS Founder Fade & Survival dataset for testing."""

import json
import random
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

OUTPUT_PATH = Path("/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/data/data_out.json")


def generate_fade_curve(project_type: str, n_months: int) -> np.ndarray:
    """Generate founder involvement share over time based on project type."""
    t = np.arange(n_months)
    
    if project_type == "smooth_fade_survive":
        # Linear decline from 0.8 to 0.1
        return np.linspace(0.8, 0.1, n_months) + np.random.normal(0, 0.03, n_months)
    
    elif project_type == "abrupt_cliff_collapse":
        # High stable then sudden drop
        stable_months = n_months - 3
        curve = np.ones(stable_months) * 0.75 + np.random.normal(0, 0.05, stable_months)
        cliff = np.linspace(0.7, 0.05, 3) + np.random.normal(0, 0.03, 3)
        return np.concatenate([curve, cliff])
    
    elif project_type == "plateau_then_cliff_collapse":
        # Plateau then sudden drop
        plateau_months = n_months - 4
        curve = np.ones(plateau_months) * 0.65 + np.random.normal(0, 0.02, plateau_months)
        cliff = np.linspace(0.6, 0.02, 4) + np.random.normal(0, 0.02, 4)
        return np.concatenate([curve, cliff])
    
    elif project_type == "gradual_fade_collapse":
        # Gradual decline but never recovers
        return np.linspace(0.7, 0.01, n_months) + np.random.normal(0, 0.04, n_months)
    
    elif project_type == "smooth_fade_collapse":
        # Smooth fade but project dies anyway (other factors)
        return np.linspace(0.75, 0.1, n_months) + np.random.normal(0, 0.03, n_months)
    
    elif project_type == "stable_high_survive":
        # Founder stays involved, project survives
        return np.ones(n_months) * 0.5 + np.random.normal(0, 0.05, n_months)
    
    else:
        return np.linspace(0.5, 0.2, n_months) + np.random.normal(0, 0.05, n_months)


def generate_post_departure(project_type: str, n_months: int = 24) -> dict:
    """Generate post-departure metrics."""
    t = np.arange(n_months)
    
    if "survive" in project_type:
        # Activity continues or grows
        base_commits = np.random.poisson(50)
        growth = 1 + t * 0.02
        noise = np.random.normal(1, 0.1, n_months)
        commits = np.maximum(0, (base_commits * growth * noise).astype(int))
        merges = np.maximum(0, (commits * 0.3 * np.random.uniform(0.8, 1.2, n_months)).astype(int))
        new_devs = np.maximum(0, (np.random.poisson(2) + t * 0.1).astype(int))
    else:
        # Activity declines to near zero
        base_commits = np.random.poisson(30)
        decay = np.exp(-t * 0.15)
        noise = np.random.normal(1, 0.2, n_months)
        commits = np.maximum(0, (base_commits * decay * noise).astype(int))
        merges = np.maximum(0, (commits * 0.1 * np.random.uniform(0.5, 1.0, n_months)).astype(int))
        new_devs = np.zeros(n_months, dtype=int)
    
    return {
        "month_index": t.tolist(),
        "total_monthly_commits": commits.tolist(),
        "total_monthly_merges": merges.tolist(),
        "new_truck_factor_developer_count": new_devs.tolist()
    }


def generate_project(project_id: str, project_type: str, idx: int) -> dict:
    """Generate a single project record."""
    n_pre_months = random.randint(12, 48)
    
    # Generate fade curve
    combined_share = generate_fade_curve(project_type, n_pre_months)
    combined_share = np.clip(combined_share, 0, 1)
    
    # Split into commit/merge/review shares
    founder_commit_share = combined_share * np.random.uniform(0.8, 1.2, n_pre_months)
    founder_merge_share = combined_share * np.random.uniform(0.7, 1.1, n_pre_months)
    founder_review_share = combined_share * np.random.uniform(0.5, 1.0, n_pre_months)
    
    founder_commit_share = np.clip(founder_commit_share, 0, 1)
    founder_merge_share = np.clip(founder_merge_share, 0, 1)
    founder_review_share = np.clip(founder_review_share, 0, 1)
    
    # Total monthly activity
    total_commits = np.random.poisson(100, n_pre_months)
    total_merges = np.random.poisson(30, n_pre_months)
    
    survival = "survive" in project_type
    
    # Departure date
    departure_date = datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1000))
    
    # Static features
    static = {
        "stars": random.randint(50, 5000) if survival else random.randint(10, 1000),
        "forks": random.randint(10, 1000) if survival else random.randint(5, 300),
        "contributor_count": random.randint(10, 100) if survival else random.randint(3, 30),
        "file_count": random.randint(100, 5000),
        "repo_age_days": random.randint(365, 3650),
        "bus_factor_at_departure": random.randint(1, 8) if survival else random.randint(1, 3)
    }
    
    pre_metrics = []
    for i in range(n_pre_months):
        pre_metrics.append({
            "month_index": i,
            "founder_commit_share": float(founder_commit_share[i]),
            "founder_merge_share": float(founder_merge_share[i]),
            "founder_review_share": float(founder_review_share[i]),
            "total_monthly_commits": int(total_commits[i]),
            "total_monthly_merges": int(total_merges[i])
        })
    
    post_metrics = generate_post_departure(project_type)
    
    return {
        "project_id": project_id,
        "founder_id": f"founder_{idx}",
        "departure_date": departure_date.isoformat(),
        "survival_label": survival,
        "pre_departure_metrics": pre_metrics,
        "post_departure_metrics": post_metrics,
        "static_features_at_departure": static
    }


def main():
    # Define project types with target counts for balanced dataset
    project_types = [
        ("smooth_fade_survive", 12),
        ("abrupt_cliff_collapse", 12),
        ("plateau_then_cliff_collapse", 10),
        ("gradual_fade_collapse", 8),
        ("smooth_fade_collapse", 6),
        ("stable_high_survive", 10),
    ]
    
    projects = []
    idx = 0
    for ptype, count in project_types:
        for _ in range(count):
            projects.append(generate_project(f"owner/repo_{idx}", ptype, idx))
            idx += 1
    
    random.shuffle(projects)
    
    data = {"examples": projects}
    
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(data, indent=2))
    print(f"Generated {len(projects)} projects to {OUTPUT_PATH}")
    
    # Print summary
    survived = sum(1 for p in projects if p["survival_label"])
    print(f"Survived: {survived}, Collapsed: {len(projects) - survived}")


if __name__ == "__main__":
    main()