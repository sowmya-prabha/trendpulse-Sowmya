import requests
import time
import json
from datetime import datetime
import os
print(os.getcwd())
headers = {"User-Agent": "TrendPulse/1.0"}
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def get_category(title):
    title = f" {title.lower()} "
    for category, keywords in CATEGORIES.items():
        for word in keywords:
            if f" {word} " in title:
                return category
    return "others" 
def fetch_data():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    try:
        ids = requests.get(url, headers=headers, timeout=5).json()[:200]  # reduced for speed
    except Exception as e:
        print("Error fetching IDs:", e)
        return []
    collected = []
    category_count = {cat: 0 for cat in CATEGORIES}
    category_count["others"] = 0
    seen_titles = set()

    for story_id in ids:
        try:
            res = requests.get(
                f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
                headers=headers,
                timeout=5
            )
            data = res.json()

            if not data or "title" not in data:
                continue

            title = data.get("title")
            if title in seen_titles:
                continue
            seen_titles.add(title)
            category = get_category(title)
            print(f"{title} --> {category}")
            story = {
                "post_id": data.get("id"),
                "title": title,
                "category": category,
                "score": data.get("score", 0),
                "num_comments": data.get("descendants", 0),
                "author": data.get("by"),
                "url": data.get("url"),
                "timestamp": data.get("time"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            if category_count.get(category, 0) < 10:
                collected.append(story)
                category_count[category] += 1

            time.sleep(0.1)

        except Exception as e:
            print(f"Error fetching {story_id}: {e}")

    print("\nTotal collected:", len(collected))
    return collected
def save_json(data):
    if not data:
        print("No data collected. File not saved.")
        return
    os.makedirs("data", exist_ok=True)
    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Saved successfully to {filename}")
    except Exception as e:
        print("Error saving file:", e)
if __name__ == "__main__":
    data = fetch_data()
    save_json(data)