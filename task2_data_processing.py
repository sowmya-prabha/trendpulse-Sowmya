import json
import pandas as pd
file_path = "data/trends_20260414.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
df = pd.DataFrame(data)

print("Original Data Shape:", df.shape)
df.drop_duplicates(subset=["title"], inplace=True)
df["title"] = df["title"].fillna("No Title")
df["author"] = df["author"].fillna("Unknown")
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)
df = df[df["title"].str.strip() != ""]
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s', errors='coerce')
df = df[df["score"] >= 5]
df["title"] = df["title"].str.strip()
df["author"] = df["author"].str.strip()
df.reset_index(drop=True, inplace=True)

print("Cleaned Data Shape:", df.shape)
output_file = "data/cleaned_trends.json"
df.to_json(output_file, orient="records", indent=4)
print(f"Cleaned data saved to {output_file}")
