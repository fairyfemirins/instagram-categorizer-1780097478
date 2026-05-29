# Technical Design

## Architecture
1. **API Layer**: Uses Instagram Basic Display API to fetch posts.
2. **Categorization**: Extracts hashtags from captions using regex.
3. **Output**: Generates JSON for programmatic use and Markdown for readability.

## Limitations
- Requires Instagram Basic Display API access (OAuth2).
- Only categorizes by hashtags (no NLP for semantic analysis).