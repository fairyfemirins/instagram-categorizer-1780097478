import unittest
from unittest.mock import patch
from src.main import InstagramCategorizer

class TestInstagramCategorizer(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_posts(self, mock_get):
        mock_get.return_value.json.return_value = {"data": [{"id": "1", "caption": "#test"}]}
        categorizer = InstagramCategorizer("token", "user_id")
        posts = categorizer.fetch_posts()
        self.assertEqual(len(posts), 1)

    def test_categorize_by_hashtag(self):
        posts = [{"caption": "#test post #demo"}, {"caption": "#demo again"}]
        categorizer = InstagramCategorizer("token", "user_id")
        categories = categorizer.categorize_by_hashtag(posts)
        self.assertEqual(len(categories["test"]), 1)
        self.assertEqual(len(categories["demo"]), 2)

if __name__ == "__main__":
    unittest.main()