import pandas as pd
import os

# Folder where the CSVs are located
data_folder = "raw_data"

# Define file names and their categories
files = {
    "business_data.csv": "business",
    "education_data.csv": "education",
    "entertainment_data.csv": "entertainment",
    "sports_data.csv": "sports",
    "technology_data.csv": "technology"
}

combined = []

for filename, category in files.items():
    path = os.path.join(data_folder, filename)
    df = pd.read_csv(path)
    df["category"] = category
    combined.append(df)

# Concatenate all dataframes
final_df = pd.concat(combined, ignore_index=True)
final_df.to_csv("data/news_dataset.csv", index=False)
print(f"Combined dataset saved with {len(final_df)} records.")
