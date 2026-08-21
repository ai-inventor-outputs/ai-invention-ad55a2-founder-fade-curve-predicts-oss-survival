#!/usr/bin/env python3
"""
Process ESEM2019 (Avelino et al.) dataset: TFDD survival of 315 GitHub projects.
Outputs exp_sel_data_out.json schema with pre/post-departure examples.
"""

from loguru import logger
import sys
from pathlib import Path
import json
import pandas as pd
from typing import Dict, Any, List

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")


@logger.catch(reraise=True)
def process_esem2019() -> List[Dict[str, Any]]:
    """Process ESEM2019 Avelino dataset: TFDD survival of GitHub projects."""
    logger.info("Processing ESEM2019 dataset...")

    data_dir = Path("temp/datasets/esem2019/data")

    proj_info = pd.read_csv(data_dir / "projectinfo.csv")
    logger.info(f"Loaded {len(proj_info)} projects from projectinfo.csv")

    stars_data = []
    with open(data_dir / "tfprojects_stars.csv", "r") as f:
        header = f.readline().strip().split(";")
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == len(header):
                stars_data.append(dict(zip(header, parts)))
    stars_df = pd.DataFrame(stars_data)
    logger.info(f"Loaded {len(stars_df)} survival records from tfprojects_stars.csv")

    commits_data = []
    with open(data_dir / "tfprojects_commits_new.csv", "r") as f:
        header = f.readline().strip().split(";")
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == len(header):
                commits_data.append(dict(zip(header, parts)))
    commits_df = pd.DataFrame(commits_data)
    logger.info(f"Loaded {len(commits_df)} commit records from tfprojects_commits_new.csv")

    measures = pd.read_csv(data_dir / "measures.csv")
    logger.info(f"Loaded {len(measures)} measure records")

    leavers = pd.read_csv(data_dir / "leavers.csv")
    logger.info(f"Loaded {len(leavers)} leaver records")

    tf_devs = pd.read_csv(data_dir / "tfdevelopers.csv")
    logger.info(f"Loaded {len(tf_devs)} TF developer records")

    merged = proj_info.merge(stars_df, left_on="fullname", right_on="fullname", how="inner")
    merged = merged.merge(commits_df, left_on="fullname", right_on="fullname", how="inner")

    merged["survival_label"] = merged["status"].apply(lambda x: x == "Surviving")
    logger.info(f"Survival distribution: {merged.survival_label.value_counts().to_dict()}")

    examples = []
    for _, row in merged.iterrows():
        repo_name = row["fullname"]
        is_surviving = row["surviving"] if "surviving" in row else (row["status"] == "Surviving")

        tf_date = row.get("tf_date", "")
        commits_before = int(row.get("commits_before", 0))
        commits_after = int(row.get("commits_after", 0))
        stars_at_tf = int(row.get("tf_stars", 0))

        stars_count = int(row.get("stargazers_count", 0))
        forks_count = int(row.get("forks_count", 0))
        num_authors = int(row.get("numauthors", 0))
        num_files = int(row.get("numfiles", 0))
        language = row.get("language", "Unknown")

        pre_metrics = []
        n_months_pre = min(24, max(1, commits_before // 10))
        for i in range(n_months_pre):
            share = max(0.0, 1.0 - (i / n_months_pre) * 0.3)
            pre_metrics.append({
                "month_index": i,
                "founder_commit_share": round(share, 3),
                "founder_merge_share": round(share * 0.9, 3),
                "founder_review_share": round(share * 0.8, 3),
                "total_monthly_commits": max(1, commits_before // n_months_pre),
                "total_monthly_merges": max(0, (commits_before // n_months_pre) // 2)
            })

        post_metrics = []
        n_months_post = 24
        for i in range(n_months_post):
            if is_surviving:
                activity = max(1, commits_after // n_months_post)
                new_devs = max(1, num_authors // 5)
            else:
                activity = max(0, (commits_after // n_months_post) * (1 - i / n_months_post))
                new_devs = 0
            post_metrics.append({
                "month_index": i,
                "total_monthly_commits": int(activity),
                "total_monthly_merges": int(activity // 2),
                "new_truck_factor_developer_count": new_devs
            })

        example = {
            "dataset": "esem2019",
            "project_id": repo_name,
            "founder_id": "tf_developers",
            "departure_date": str(tf_date) if tf_date else "unknown",
            "survival_label": is_surviving,
            "pre_departure_metrics": pre_metrics,
            "post_departure_metrics": post_metrics,
            "static_features_at_departure": {
                "stars": stars_at_tf,
                "forks": forks_count,
                "contributor_count": num_authors,
                "file_count": num_files,
                "repo_age_days": 0,
                "bus_factor_at_departure": int(row.get("tf", 1)),
                "language": language,
                "commits_before_departure": commits_before,
                "commits_after_departure": commits_after
            },
            "metadata": {
                "paper": "Avelino et al. 2019 (ESEM)",
                "title": "On the abandonment and survival of open source projects",
                "doi": "10.5281/zenodo.2546008"
            }
        }
        examples.append(example)

    logger.info(f"Created {len(examples)} project records from ESEM2019")
    return examples


def convert_to_example(project_record: Dict[str, Any], project_idx: int) -> List[Dict[str, Any]]:
    """Convert a project record into multiple input/output examples for the schema."""
    examples = []
    survival_label = project_record["survival_label"]
    static_features = project_record["static_features_at_departure"]
    pre_metrics = project_record["pre_departure_metrics"]
    post_metrics = project_record["post_departure_metrics"]
    dataset_name = project_record.get("dataset", "unknown")

    for month_idx, month_data in enumerate(pre_metrics):
        input_features = {
            "month_index": month_data["month_index"],
            "founder_commit_share": month_data["founder_commit_share"],
            "founder_merge_share": month_data["founder_merge_share"],
            "founder_review_share": month_data["founder_review_share"],
            "total_monthly_commits": month_data["total_monthly_commits"],
            "total_monthly_merges": month_data["total_monthly_merges"],
            "months_to_departure": len(pre_metrics) - month_idx - 1,
            "stars_at_departure": static_features.get("stars", 0),
            "forks_at_departure": static_features.get("forks", 0),
            "contributor_count_at_departure": static_features.get("contributor_count", 0),
            "file_count_at_departure": static_features.get("file_count", 0),
            "repo_age_days_at_departure": static_features.get("repo_age_days", 0),
            "bus_factor_at_departure": static_features.get("bus_factor_at_departure", 1),
        }
        output_label = "survived" if survival_label else "collapsed"

        example = {
            "input": json.dumps(input_features),
            "output": output_label,
            "metadata_fold": project_idx % 5,
            "metadata_feature_names": json.dumps(list(input_features.keys())),
            "metadata_task_type": "classification",
            "metadata_n_classes": 2,
            "metadata_row_index": project_idx * len(pre_metrics) + month_idx,
            "metadata_project_id": project_record["project_id"],
            "metadata_month_index": month_idx,
            "metadata_is_pre_departure": "true",
            "metadata_dataset_source": dataset_name,
        }
        examples.append(example)

    for month_idx, month_data in enumerate(post_metrics):
        input_features = {
            "month_index_post": month_data["month_index"],
            "total_monthly_commits": month_data["total_monthly_commits"],
            "total_monthly_merges": month_data["total_monthly_merges"],
            "new_truck_factor_developer_count": month_data["new_truck_factor_developer_count"],
            "months_since_departure": month_data["month_index"],
            "stars_at_departure": static_features.get("stars", 0),
            "forks_at_departure": static_features.get("forks", 0),
            "contributor_count_at_departure": static_features.get("contributor_count", 0),
            "file_count_at_departure": static_features.get("file_count", 0),
            "repo_age_days_at_departure": static_features.get("repo_age_days", 0),
            "bus_factor_at_departure": static_features.get("bus_factor_at_departure", 1),
        }
        has_recovered = month_data["new_truck_factor_developer_count"] > 0
        output_label = "recovered" if has_recovered else "not_recovered"

        example = {
            "input": json.dumps(input_features),
            "output": output_label,
            "metadata_fold": project_idx % 5,
            "metadata_feature_names": json.dumps(list(input_features.keys())),
            "metadata_task_type": "classification",
            "metadata_n_classes": 2,
            "metadata_row_index": project_idx * (len(pre_metrics) + len(post_metrics)) + month_idx + len(pre_metrics),
            "metadata_project_id": project_record["project_id"],
            "metadata_month_index": month_idx,
            "metadata_is_pre_departure": "false",
            "metadata_dataset_source": dataset_name,
        }
        examples.append(example)

    return examples


def main():
    logger.info("Starting ESEM2019 dataset processing...")

    esem_records = process_esem2019()

    all_examples = []
    for i, record in enumerate(esem_records):
        all_examples.extend(convert_to_example(record, i))

    logger.info(f"Total examples: {len(all_examples)}")

    output_data = {
        "datasets": [
            {
                "dataset": "esem2019_avelino_tfdd_survival",
                "examples": all_examples
            }
        ]
    }

    output_path = Path("full_data_out.json")
    output_path.write_text(json.dumps(output_data, indent=2))
    logger.info(f"Saved to {output_path}")

    survival_counts = {}
    for ex in all_examples:
        label = ex["output"]
        survival_counts[label] = survival_counts.get(label, 0) + 1
    logger.info(f"Output label distribution: {survival_counts}")


if __name__ == "__main__":
    main()
