#!/usr/bin/env python3
"""Generate a synthetic dataset for OSS founder departure and survival as a top-level array."""

import json
import random
from pathlib import Path
from loguru import logger

# Configure logger
logger.remove()
logger.add(lambda msg: print(msg, end=""), level="INFO")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

def generate_synthetic_project(project_idx: int) -> dict:
    """Generate a single synthetic project."""
    # Project ID
    project_id = f"oss_project_{project_idx:03d}"
    
    # Founder ID (anonymized)
    founder_id = f"founder_{random.randint(1000, 9999)}"
    
    # Number of months of founder activity (from project inception to departure)
    num_months = random.randint(6, 36)  # 6 to 36 months
    
    # Generate monthly shares: founder's share of commits, merges, reviews
    # We'll simulate a decreasing trend over time
    monthly_founders_share_commits = []
    monthly_founders_share_merges = []
    monthly_founders_share_reviews = []
    
    base_share = random.uniform(0.3, 0.8)  # Founder starts with 30-80% share
    for month in range(num_months):
        # Simulate decay: founder's share decreases over time
        decay_factor = 1 - (month / num_months) * random.uniform(0.5, 0.9)
        share = base_share * decay_factor
        # Add some noise
        share = max(0.0, min(1.0, share + random.uniform(-0.1, 0.1)))
        
        monthly_founders_share_commits.append(round(share, 3))
        # Merges and reviews might be slightly different
        monthly_founders_share_merges.append(round(share * random.uniform(0.8, 1.2), 3))
        monthly_founders_share_reviews.append(round(share * random.uniform(0.8, 1.2), 3))
    
    # Static features at departure
    contributor_count = random.randint(5, 50)
    # Bus factor: minimum number of contributors contributing 50% of commits
    bus_factor = random.randint(1, min(5, contributor_count))
    project_age_months = num_months + random.randint(0, 12)  # Project might be older than founder's activity
    star_count = random.randint(10, 10000)
    file_count = random.randint(100, 5000)
    
    static_features = {
        "bus_factor": bus_factor,
        "contributor_count": contributor_count,
        "project_age_months": project_age_months,
        "star_count": star_count,
        "file_count": file_count
    }
    
    # Survival label: binary (0 for collapsed, 1 for survived)
    # Let's make survival depend on some features
    survival_score = (
        0.3 * (1 - bus_factor / contributor_count) +  # Lower bus factor -> riskier
        0.3 * (contributor_count / 50) +              # More contributors -> better
        0.2 * (project_age_months / 60) +             # Older project -> better
        0.2 * (star_count / 10000)                    # More stars -> better
    )
    survival_label = 1 if survival_score > 0.5 else 0
    
    # Continuous survival metric: post-departure commit volume normalized to pre-departure baseline
    # We'll simulate: if survived, higher post-departure activity
    pre_departure_avg_commits = random.randint(10, 100)  # Average monthly commits before departure
    if survival_label == 1:
        post_departure_total_commits = pre_departure_avg_commits * num_months * random.uniform(0.8, 1.5)
    else:
        post_departure_total_commits = pre_departure_avg_commits * num_months * random.uniform(0.0, 0.3)
    
    continuous_survival_metric = post_departure_total_commits / (pre_departure_avg_commits * num_months)
    continuous_survival_metric = round(continuous_survival_metric, 3)
    
    return {
        "project_id": project_id,
        "founder_id": founder_id,
        "monthly_founders_share_commits": monthly_founders_share_commits,
        "monthly_founders_share_merges": monthly_founders_share_merges,
        "monthly_founders_share_reviews": monthly_founders_share_reviews,
        "static_features_at_departure": static_features,
        "survival_label": survival_label,
        "continuous_survival_metric": continuous_survival_metric
    }

def main():
    """Generate dataset and save to file."""
    logger.info("Generating synthetic dataset for OSS founder departure and survival")
    
    # Number of projects
    num_projects = 20
    
    # Generate a list of projects (top-level array)
    projects = []
    for i in range(num_projects):
        project = generate_synthetic_project(i)
        projects.append(project)
        if (i + 1) % 5 == 0:
            logger.info(f"Generated {i + 1}/{num_projects} projects")
    
    # Save to JSON file
    output_path = Path("full_dataset.json")
    logger.info(f"Saving dataset to {output_path}")
    output_path.write_text(json.dumps(projects, indent=2))
    
    logger.info(f"Dataset saved with {len(projects)} projects")

if __name__ == "__main__":
    main()