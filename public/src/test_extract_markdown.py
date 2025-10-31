import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Images: ![first](http://example.com/1.png) and ![second](http://example.com/2.jpg)"
        )
        self.assertListEqual(
            [("first", "http://example.com/1.png"), ("second", "http://example.com/2.jpg")],
            matches
        )

    def test_extract_markdown_images_empty_alt(self):
        matches = extract_markdown_images(
            "An image with no alt: ![](https://example.com/no-alt.png)"
        )
        self.assertListEqual([("", "https://example.com/no-alt.png")], matches)

    def test_extract_markdown_images_complex_url(self):
        matches = extract_markdown_images(
            "Complex URL: ![alt](https://example.com/path/to/image?query=1&foo=bar#hash)"
        )
        self.assertListEqual(
            [("alt", "https://example.com/path/to/image?query=1&foo=bar#hash")],
            matches
        )

    def test_extract_markdown_images_not_an_image(self):
        matches = extract_markdown_images(
            "This is not an image: [text](https://example.com/page)"
        )
        self.assertListEqual([], matches)

