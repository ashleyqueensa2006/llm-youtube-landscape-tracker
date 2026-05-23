import json
import pandas as pd

with open("data/videos.json") as f:
    videos = json.load(f)

df = pd.DataFrame(videos)
html = df.to_html(index=False, escape=False)

with open("templates/index.html", "w") as f:
    f.write(f"""
    <html>
    <head><title>LLM YouTube Landscape</title>
    <style>table {{border-collapse: collapse; width: 100%;}} th, td {{border: 1px solid #ccc; padding: 8px;}}</style>
    </head>
    <body>
    <h1>LLM YouTube Content Tracker</h1>
    <p>Last updated: {pd.Timestamp.now()}</p>
    {html}
    </body></html>
    """)

print("Table generated!")
