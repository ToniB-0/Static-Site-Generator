import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextType

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **bold** and _italic_ with a `code`."
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[5].text_type, TextType.CODE)

