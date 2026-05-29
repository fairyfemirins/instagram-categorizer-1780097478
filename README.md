# Instagram Post Auto-Categorizer

Autonomously categorize Instagram posts into folders using hashtags or NLP.

## Features
- Fetches posts from Instagram API (or use mock data for testing).
- Categorizes posts into user-defined folders (e.g., `travel`, `food`).
- Falls back to NLP (spaCy) if hashtags are missing.
- Saves post URLs and captions to text files.

## Setup
1. **Install dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

2. **Configure `.env`**:
   ```ini
   INSTAGRAM_ACCESS_TOKEN=your_token_here
   INSTAGRAM_USER_ID=your_user_id_here
   DEFAULT_CATEGORIES=travel,food,tech,fashion,fitness
   ```

3. **Run**:
   ```bash
   python categorizer.py
   ```

## Output
Posts are saved to `~/instagram_categories/` in category-specific folders.

## License
MIT