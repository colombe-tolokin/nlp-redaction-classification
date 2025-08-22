import pandas as pd
import os
import yaml
import logging

def load_config(config_path="config.yaml"):
    """
    Load configuration settings from a YAML file.
    Args:
        config_path (str): Path to the config file.
    Returns:
        dict: Configuration parameters.
    """
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def setup_logging(level="INFO"):
    """
    Set up logging configuration.
    Args:
        level (str): Logging level as a string.
    """
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=getattr(logging, level.upper(), logging.INFO)
    )

def combine_raw_data(config):
    """
    Combine raw CSV files from different categories into a single DataFrame.
    Args:
        config (dict): Configuration parameters.
    Returns:
        pd.DataFrame: Combined DataFrame.
    """
    # Define file names and their categories
    files = {
        "business_data.csv": "business",
        "education_data.csv": "education",
        "entertainment_data.csv": "entertainment",
        "sports_data.csv": "sports",
        "technology_data.csv": "technology"
    }

    combined = []
    data_folder = config["data_folder"]

    for filename, category in files.items():
        path = os.path.join(data_folder, filename)
        logging.info(f"Reading {path}")
        df = pd.read_csv(path)
        df["category"] = category
        combined.append(df)

    final_df = pd.concat(combined, ignore_index=True)
    return final_df

def main():
    config = load_config()
    setup_logging(config.get("log_level", "INFO"))
    logging.info("Starting data combination process.")

    final_df = combine_raw_data(config)
    output_file = config["output_file"]
    final_df.to_csv(output_file, index=False)
    logging.info(f"Combined dataset saved to {output_file} with {len(final_df)} records.")

if __name__ == "__main__":
    main()