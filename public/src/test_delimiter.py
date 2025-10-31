import unittest
from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestDelimiter(unittest.TestCase):
    def test_basic_code_delimiter(self):
        nodes = [TextNode("`code`", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result[0].text_type, TextType.CODE)

    def test_multiple_code_blocks(self):
        nodes = [TextNode("`code1` and `code2`", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len([n for n in result if n.text_type == TextType.CODE]), 2)

    def test_bold_text_delimiter(self):
        nodes = [TextNode("**bold**", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result[0].text_type, TextType.BOLD)

    def test_italic_text_delimiter(self):
        nodes = [TextNode("_italic_", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(result[0].text_type, TextType.ITALIC)

    def test_unmatched_delimiter_raises(self):
        nodes = [TextNode("**bold", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_non_text_nodes_unchanged(self):
        node = TextNode("text", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result[0], node)

    def test_empty_text_between_delimiters(self):
        nodes = [TextNode("**", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_multiple_nodes_input(self):
        nodes = [TextNode("hello **bold** world", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 3)

