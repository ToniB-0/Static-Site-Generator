import unittest
from block_to_block_type import block_to_block_type
from block_type import BlockType

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        md = "# Heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_code_block(self):
        md = "```\ncode\n```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_quote_block(self):
        md = "> quote"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_unordered_list(self):
        md = "- item1\n- item2"
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        md = "1. one\n2. two"
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        md = "Just a paragraph."
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

