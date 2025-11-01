import unittest
from textnode import TextNode, TextType
from split_nodes_markdown import split_nodes_image, split_nodes_link

class TestSplitNodesMarkdown(unittest.TestCase):
    def test_split_nodes_image_basic(self):
        node = TextNode("Look ![alt](url.png) here", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Look ")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "url.png")
        self.assertEqual(result[2].text, " here")

    def test_split_nodes_link_basic(self):
        node = TextNode("Click [me](link.com) now", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "link.com")

if __name__ == "__main__":
    unittest.main()

