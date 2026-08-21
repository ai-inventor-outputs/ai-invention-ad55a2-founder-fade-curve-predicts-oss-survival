#!/usr/bin/env python3
"""Load OSS founder departure dataset and convert to exp_sel_data_out.json format."""

import json
from pathlib import Path
from loguru import logger

# Configure logger
logger.remove()
logger.add(lambda msg: print(msg, end=""), level="INFO")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

def load_and_convert_dataset():
    """Load the synthetic dataset and convert to required format."""
    logger.info("Loading synthetic OSS founder departure dataset")
    
    # Load the full dataset
    dataset_path = Path("full_dataset.json")
    if not dataset_path.exists():
        logger.error(f"Dataset file not found: {dataset_path}")
        raise FileNotFoundError(f"Dataset file not found: {dataset_path}")
    
    with open(dataset_path) as f:
        projects = json.load(f)
    
    logger.info(f"Loaded {len(projects)} projects")
    
    # Convert to exp_sel_data_out.json format
    examples = []
    
    for idx, project in enumerate(projects):
        # Prepare input: all features except survival_label (which is our target)
        input_features = {
            "project_id": project["project_id"],
            "founder_id": project["founder_id"],
            "monthly_founders_share_commits": project["monthly_founders_share_commits"],
            "monthly_founders_share_merges": project["monthly_founders_share_merges"],
            "monthly_founders_share_reviews": project["monthly_founders_share_reviews"],
            "static_features_at_departure": project["static_features_at_departure"],
            "continuous_survival_metric": project["continuous_survival_metric"]
        }
        
        # Output is the survival_label (as string)
        output = str(project["survival_label"])
        
        # Create example
        example = {
            "input": json.dumps(input_features),
            "output": output,
            # Optional metadata fields
            "metadata_row_index": idx,
            "metadata_task_type": "classification",
            "metadata_n_classes": 2,
            "metadata_feature_names": [
                "project_id", "founder_id", "monthly_founders_share_commits",
                "monthly_founders_share_merges", "monthly_founders_share_reviews",
                "static_features_at_departure", "continuous_survival_metric"
            ]
        }
        
        examples.append(example)
    
    # Create the final dataset structure
    result = {
        "datasets": [
            {
                "dataset": "oss_founder_departure",
                "examples": examples
            }
        ]
    }
    
    logger.info(f"Converted {len(examples)} examples to exp_sel_data_out format")
    return result

def main():
    """Main function to generate full_data_out.json."""
    try:
        # Load and convert dataset
        data = load_and_convert_dataset()
        
        # Save to full_data_out.json
        output_path = Path("full_data_out.json")
        logger.info(f"Saving converted data to {output_path}")
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info("Successfully generated full_data_out.json")
        
    except Exception as e:
        logger.error(f"Error in data.py: {e}")
        raise

if __name__ == "__main__":
    main()