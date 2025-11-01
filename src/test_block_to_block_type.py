import unittest
from block_to_block_type import block_to_block_type
from block_type import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Subheading level 3"), BlockType.HEADING)

    def test_code_block(self):
        code = "```\nprint('hello world')\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote_block(self):
        quote = "> This is a quote\n> Continued quote line"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_unordered_list(self):
        ul = "- First item\n- Second item\n- Third item"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ol = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        paragraph = "This is a normal paragraph of text without any markdown indicators."
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()

