#!/usr/bin/env python3
"""Load 2 GitHub repo datasets, standardize features, and output exp_sel_data_out.json schema."""

from loguru import logger
from pathlib import Path
import json
import sys
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WORKSPACE = Path(__file__).resolve().parent
TEMP_DIR = WORKSPACE / "temp" / "datasets"
OUTPUT = WORKSPACE / "full_data_out.json"


@logger.catch(reraise=True)
def main():
    now = datetime.now(tz=None)
    one_year_ago = now - timedelta(days=365)

    # ── Dataset 1: h1alexbel/github-repos ──────────────────────────────
    logger.info("Loading h1alexbel/github-repos CSV...")
    csv_path = TEMP_DIR / "h1alexbel_github-repos_results.csv"
    df1 = pd.read_csv(csv_path, low_memory=False)
    logger.info(f"  Loaded {len(df1)} rows, columns: {list(df1.columns)}")

    examples_1 = []
    for idx, row in df1.iterrows():
        try:
            repo_full = str(row.get("repo", ""))
            if not repo_full or repo_full == "nan":
                continue

            # Parse dates — strip timezone info for consistent comparison
            created = pd.to_datetime(row.get("createdAt", pd.NaT), errors="coerce")
            last_commit = pd.to_datetime(row.get("lastCommitDate", pd.NaT), errors="coerce")
            if pd.notna(last_commit) and last_commit.tzinfo is not None:
                last_commit = last_commit.tz_localize(None)
            if pd.notna(created) and created.tzinfo is not None:
                created = created.tz_localize(None)

            # Proxy survival label: use activity ratio and contributor count
            # SURVIVE proxy: repo has multiple contributors AND recent activity
            # COLLAPSE proxy: repo has few contributors AND stale activity
            contributors = int(row["contributors"]) if pd.notna(row["contributors"]) else 0
            commits = int(row["commits"]) if pd.notna(row["commits"]) else 0
            stars = int(row["stars"]) if pd.notna(row["stars"]) else 0

            if pd.notna(last_commit) and pd.notna(created):
                age_days = (last_commit - created).days
                if age_days > 0:
                    activity_ratio = commits / max(age_days, 1)
                else:
                    activity_ratio = 0
            else:
                activity_ratio = 0

            # Heuristic: ACTIVE if contributors > 5 OR (high stars AND decent activity)
            if contributors >= 5 or (stars >= 1000 and activity_ratio >= 0.5):
                label = "ACTIVE"
            elif contributors <= 2 and activity_ratio < 0.1:
                label = "INACTIVE"
            else:
                label = "ACTIVE"  # default to active for ambiguous cases

            # Build feature dict (clean NaNs)
            features = {
                "repo": repo_full,
                "branch": str(row.get("branch", "")) if pd.notna(row.get("branch")) else "",
                "description": str(row.get("description", ""))[:200] if pd.notna(row.get("description")) else "",
                "topics": str(row.get("topics", "")) if pd.notna(row.get("topics")) else "",
                "created_at": str(created) if pd.notna(created) else "",
                "last_commit_date": str(last_commit) if pd.notna(last_commit) else "",
                "last_release_date": str(row.get("lastReleaseDate", "")) if pd.notna(row.get("lastReleaseDate")) else "",
                "contributors": int(row["contributors"]) if pd.notna(row["contributors"]) else 0,
                "pulls": int(row["pulls"]) if pd.notna(row["pulls"]) else 0,
                "commits": int(row["commits"]) if pd.notna(row["commits"]) else 0,
                "issues": int(row["issues"]) if pd.notna(row["issues"]) else 0,
                "forks": int(row["forks"]) if pd.notna(row["forks"]) else 0,
                "stars": int(row["stars"]) if pd.notna(row["stars"]) else 0,
                "disk_usage": float(row["diskUsage"]) if pd.notna(row["diskUsage"]) else 0.0,
                "license": str(row.get("license", "")) if pd.notna(row.get("license")) else "",
                "language": str(row.get("language", "")) if pd.notna(row.get("language")) else "",
            }

            feature_names = list(features.keys())
            fold = idx % 5

            examples_1.append({
                "input": json.dumps(features),
                "output": label,
                "metadata_fold": fold,
                "metadata_feature_names": feature_names,
                "metadata_task_type": "classification",
                "metadata_n_classes": 2,
                "metadata_row_index": int(idx),
                "metadata_dataset_source": "h1alexbel/github-repos",
                "metadata_repo_full_name": repo_full,
            })
        except Exception as e:
            logger.warning(f"  Skipping row {idx}: {e}")
            continue

    logger.info(f"  Built {len(examples_1)} examples from h1alexbel")

    # ── Assemble output (using only h1alexbel — best dataset for domain) ──
    output = {
        "metadata": {
            "description": "GitHub OSS repository metadata for Founder Fade hypothesis testing. Contains repo-level features and proxy survival labels (ACTIVE/INACTIVE).",
            "source_datasets": [
                "h1alexbel/github-repos (14,428 repos, MIT license, collected via ghminer tool)"
            ],
            "chosen_dataset": "h1alexbel/github-repos",
            "selection_rationale": "Chosen over AmanPriyanshu/random-small-github-repositories due to: (1) larger coverage (14K vs 5.6K repos), (2) richer features (contributors, commits, pulls, issues, forks, stars, language, dates), (3) broader ecosystem (not limited to Android/Java), (4) confirmed provenance via ghminer GitHub repo.",
            "label_definition": "ACTIVE if contributors>=5 OR (stars>=1000 AND activity_ratio>=0.5); INACTIVE if contributors<=2 AND activity_ratio<0.1. Proxy labels for downstream Founder Fade analysis.",
            "total_examples": len(examples_1),
            "created_at": now.isoformat(),
        },
        "datasets": [
            {
                "dataset": "h1alexbel/github-repos",
                "examples": examples_1,
            },
        ],
    }

    # Write output
    logger.info(f"Writing {len(examples_1)} examples to {OUTPUT}...")
    OUTPUT.write_text(json.dumps(output, indent=2))
    logger.info(f"Done! File size: {OUTPUT.stat().st_size / 1e6:.1f} MB")

    # Summary stats
    active_1 = sum(1 for e in examples_1 if e["output"] == "ACTIVE")
    logger.info(f"  h1alexbel: {active_1} ACTIVE / {len(examples_1) - active_1} INACTIVE")


if __name__ == "__main__":
    main()
