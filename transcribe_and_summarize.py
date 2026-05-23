import json
import os
from openai import OpenAI
from config import AI_MODEL

client = OpenAI()  # Uses OPENAI_API_KEY from environment

def summarize_video(title, description=""):
    prompt = f"""Summarize what this video says about Large Language Models.
    Title: {title}
    Description: {description}
    
    Return in this format:
    Topics: [list of topics]
    Key Points: [bullet points]
    Relation to other creators: [brief]
    """
    
    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example usage (expand this)
print("Summarization ready. Add logic to process videos here.")
