import unittest
from markdown_to_block import markdown_to_blocks

class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = "# Heading\n\nParagraph text\n\n- list1\n- list2"
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "# Heading")
        self.assertEqual(blocks[1], "Paragraph text")
        self.assertEqual(blocks[2], "- list1\n- list2")

