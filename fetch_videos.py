import feedparser
import json
import os
from datetime import datetime
from config import CHANNELS

DATA_FILE = "data/videos.json"
os.makedirs("data", exist_ok=True)

def fetch_channel_videos(channel_name, channel_id):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    feed = feedparser.parse(url)
    videos = []
    
    for entry in feed.entries[:10]:  # Last 10 videos
        videos.append({
            "channel": channel_name,
            "title": entry.title,
            "url": entry.link,
            "published": entry.published,
            "video_id": entry.yt_videoid,
            "timestamp": datetime.now().isoformat()
        })
    return videos

all_videos = []
for name, cid in CHANNELS.items():
    print(f"Fetching from {name}...")
    all_videos.extend(fetch_channel_videos(name, cid))

# Save
with open(DATA_FILE, "w") as f:
    json.dump(all_videos, f, indent=2)

print(f"Saved {len(all_videos)} videos.")
