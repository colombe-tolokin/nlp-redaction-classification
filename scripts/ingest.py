import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} records.")
    return df

if __name__ == "__main__":
    df = load_data("data/news_dataset.csv")
