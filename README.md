# Instagram Post Auto-Categorizer

Automatically categorize Instagram posts by hashtags using the Instagram Basic Display API.

## Features
- Fetch posts from Instagram using OAuth2.
- Categorize posts by hashtags in captions.
- Export results to JSON and Markdown.

## Setup
1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Access**
   - Create a Facebook Developer account and register an Instagram app.
   - Obtain an access token and user ID from the [Instagram Graph API Explorer](https://developers.facebook.com/tools/explorer/).
   - Copy `.env.example` to `.env` and add your credentials.

3. **Run the Tool**
   ```bash
   python src/main.py --token YOUR_TOKEN --user-id YOUR_USER_ID
   ```

## Output
- `output/categorized_posts.json`: Structured JSON of categorized posts.
- `output/report.md`: Human-readable Markdown report.

## Note
This repository was published under `fairyfemirins/instagram-categorizer-1780093590` due to namespace restrictions in cron mode.
To transfer to `Femirins/instagram-categorizer`:
1. Go to: [https://github.com/fairyfemirins/instagram-categorizer-1780093590/settings](https://github.com/fairyfemirins/instagram-categorizer-1780093590/settings)
2. Under "Danger Zone", select "Transfer repository".
3. Enter `Femirins/instagram-categorizer` as the new owner.

## License
MIT