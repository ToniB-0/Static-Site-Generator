# src/test_extract_title.py
import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_whitespace(self):
        self.assertEqual(extract_title("#   Hello World   "), "Hello World")

    def test_multiple_titles_uses_first(self):
        md = "# First Title\n\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")

    def test_no_title_raises(self):
        with self.assertRaises(ValueError):
            extract_title("No heading here\nJust text")

if __name__ == "__main__":
    unittest.main()

