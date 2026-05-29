#!/usr/bin/env python3
"""
Autonomous Instagram Post Auto-Categorizer
Fetches Instagram posts and categorizes them into folders based on hashtags or NLP.
"""

import os
import re
import shutil
from pathlib import Path
from dotenv import load_dotenv
import requests
import spacy
from typing import Dict, List, Optional

# Load environment variables
load_dotenv()

# Constants
ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
USER_ID = os.getenv("INSTAGRAM_USER_ID")
DEFAULT_CATEGORIES = os.getenv("DEFAULT_CATEGORIES", "travel,food,tech").split(",")
OUTPUT_DIR = Path.home() / "instagram_categories"

# Load NLP model
nlp = spacy.load("en_core_web_sm")


def fetch_instagram_posts() -> List[Dict]:
    """Fetch Instagram posts from the Graph API."""
    url = f"https://graph.instagram.com/{USER_ID}/media"
    params = {
        "fields": "id,caption,media_url,permalink",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("data", [])


def extract_hashtags(caption: str) -> List[str]:
    """Extract hashtags from a caption."""
    return [tag.lower() for tag in re.findall(r"#(\w+)", caption)] if caption else []


def categorize_post(caption: str, hashtags: List[str]) -> str:
    """Categorize post using hashtags or NLP."""
    # Prioritize hashtags
    for tag in hashtags:
        if tag in DEFAULT_CATEGORIES:
            return tag
    
    # Fallback to NLP
    doc = nlp(caption)
    for token in doc:
        if token.text.lower() in DEFAULT_CATEGORIES:
            return token.text.lower()
    
    return "uncategorized"


def save_post(post: Dict, category: str) -> None:
    """Save post metadata to a category folder."""
    category_dir = OUTPUT_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    
    # Save post URL to a text file
    post_file = category_dir / f"{post['id']}.txt"
    with open(post_file, "w") as f:
        f.write(f"URL: {post['permalink']}\n")
        if post.get("caption"):
            f.write(f"Caption: {post['caption']}\n")


def main():
    """Main workflow."""
    print("🔍 Fetching Instagram posts...")
    posts = fetch_instagram_posts()
    
    for post in posts:
        caption = post.get("caption", "")
        hashtags = extract_hashtags(caption)
        category = categorize_post(caption, hashtags)
        save_post(post, category)
        print(f"✅ Post {post['id']} -> Category: {category}")
    
    print(f"📁 All posts saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()