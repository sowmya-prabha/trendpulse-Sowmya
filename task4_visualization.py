import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("data/cleaned_trends.csv")

print("🔹 Data Loaded:", df.shape)


# 1. NumPy Statistics

scores = df["score"].values
comments = df["num_comments"].values

print("\n📊 NumPy Statistics:")

print("👉 Score Mean:", np.mean(scores))
print("👉 Score Median:", np.median(scores))

print("👉 Comments Mean:", np.mean(comments))
print("👉 Comments Median:", np.median(comments))


# 2. Category Distribution

category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind='bar')
plt.title("Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()



# 3. Score Distribution

plt.figure()
plt.hist(df["score"], bins=10)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()


# 4. Comments Distribution

plt.figure()
plt.hist(df["num_comments"], bins=10)
plt.title("Comments Distribution")
plt.xlabel("Number of Comments")
plt.ylabel("Frequency")
plt.show()



# 5. Score vs Comments Scatter

plt.figure()
plt.scatter(df["score"], df["num_comments"])
plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Comments")
plt.show()