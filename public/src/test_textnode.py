import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_equal_same_text_type_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_type(self):
        node3 = TextNode("Test for different Type", TextType.ITALIC)
        node4 = TextNode("Test for different Type", TextType.TEXT)
        self.assertNotEqual(node3, node4)

    def test_not_equal_different_text(self):
        node5 = TextNode("Test for different TEXT", TextType.ITALIC)
        node6 = TextNode("What it says above", TextType.ITALIC)
        self.assertNotEqual(node5, node6)

    def test_not_equal_different_url(self):
        node7 = TextNode("Click me", TextType.LINK, "https://a.com")
        node8 = TextNode("Click me", TextType.LINK, None)
        self.assertNotEqual(node7, node8)





if __name__ == "__main__":
    unittest.main()
