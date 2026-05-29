#!/usr/bin/env python3
"""
Test script for Instagram Categorizer (simulates API response).
"""

import json
from pathlib import Path
from categorizer import extract_hashtags, categorize_post, save_post

# Mock Instagram API response
MOCK_POSTS = [
    {
        "id": "1",
        "caption": "Just back from Bali! #travel #vacation",
        "permalink": "https://instagram.com/p/1",
    },
    {
        "id": "2",
        "caption": "Avocado toast for breakfast 🥑 #food #healthy",
        "permalink": "https://instagram.com/p/2",
    },
    {
        "id": "3",
        "caption": "New Python library released! #tech #coding",
        "permalink": "https://instagram.com/p/3",
    },
]


def test_categorizer():
    """Test categorizer functions."""
    for post in MOCK_POSTS:
        caption = post.get("caption", "")
        hashtags = extract_hashtags(caption)
        category = categorize_post(caption, hashtags)
        save_post(post, category)
        print(f"✅ Post {post['id']} -> Category: {category}")


if __name__ == "__main__":
    test_categorizer()