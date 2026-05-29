import os
import json
import requests
from collections import defaultdict

class InstagramCategorizer:
    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id
        self.base_url = f"https://graph.instagram.com/{self.user_id}"

    def fetch_posts(self):
        """Fetch user's Instagram posts using the Basic Display API."""
        url = f"{self.base_url}/media"
        params = {
            "fields": "id,caption,media_url,permalink",
            "access_token": self.access_token
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("data", [])

    def categorize_by_hashtag(self, posts):
        """Categorize posts by hashtags in their captions."""
        categories = defaultdict(list)
        for post in posts:
            if not post.get("caption"):
                continue
            hashtags = [
                word.strip("#").lower()
                for word in post["caption"].split()
                if word.startswith("#")
            ]
            for tag in hashtags:
                categories[tag].append(post)
        return dict(categories)

    def save_results(self, categories, output_dir="output"):
        """Save categorized posts to JSON and Markdown files."""
        os.makedirs(output_dir, exist_ok=True)
        with open(f"{output_dir}/categorized_posts.json", "w") as f:
            json.dump(categories, f, indent=2)

        with open(f"{output_dir}/report.md", "w") as f:
            f.write("# Instagram Post Categorization Report\n\n")
            for tag, posts in categories.items():
                f.write(f"## #{tag}\n")
                f.write(f"**Posts:** {len(posts)}\n\n")
                for post in posts:
                    f.write(f"- [Post]({post['permalink']})\n")
                    if post.get("caption"):
                        f.write(f"  > {post['caption'][:100]}...\n")
                f.write("\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Categorize Instagram posts by hashtag.")
    parser.add_argument("--token", required=True, help="Instagram Basic Display API access token")
    parser.add_argument("--user-id", required=True, help="Instagram user ID")
    args = parser.parse_args()

    categorizer = InstagramCategorizer(args.token, args.user_id)
    posts = categorizer.fetch_posts()
    categories = categorizer.categorize_by_hashtag(posts)
    categorizer.save_results(categories)
    print(f"Categorized {len(posts)} posts into {len(categories)} hashtags.")