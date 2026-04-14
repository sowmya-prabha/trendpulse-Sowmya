import json
import pandas as pd

# Load JSON file
file_path = "data/trends_20260414.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print("🔹 Original Data Shape:", df.shape)

# 1. Remove Duplicates
df.drop_duplicates(subset=["title"], inplace=True)

# 2. Handle Missing Values
df["title"] = df["title"].fillna("No Title")
df["author"] = df["author"].fillna("Unknown")
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)

df = df[df["title"].str.strip() != ""]

# 3. Fix Data Types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s', errors='coerce')

# 4. Remove Low Quality Stories
df = df[df["score"] >= 5]

# 5. Remove White Spaces
df["title"] = df["title"].str.strip()
df["author"] = df["author"].str.strip()

# 6. Reset Index
df.reset_index(drop=True, inplace=True)

print("✅ Cleaned Data Shape:", df.shape)

# 7. Save as CSV
csv_file = "data/cleaned_trends.csv"
df.to_csv(csv_file, index=False, encoding="utf-8")

print(f"✅ Cleaned data saved to {csv_file}")