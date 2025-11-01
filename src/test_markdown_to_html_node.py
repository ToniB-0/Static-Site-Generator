import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph_block(self):
        md = "This is a paragraph with **bold** and _italic_ text."
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p></div>")

    def test_heading_block(self):
        md = "# Heading One"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h1>Heading One</h1></div>")

    def test_quote_block(self):
        md = "> This is a quote"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><blockquote>This is a quote</blockquote></div>")

    def test_unordered_list_block(self):
        md = "- item one\n- item two"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><ul><li>item one</li><li>item two</li></ul></div>")

    def test_ordered_list_block(self):
        md = "1. first\n2. second"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><ol><li>first</li><li>second</li></ol></div>")

    def test_code_block(self):
        md = "```\nprint('Hello')\n```"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><pre><code>print('Hello')</code></pre></div>")

