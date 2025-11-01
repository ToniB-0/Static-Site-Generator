import re
from markdown_to_block import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from converters import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import ParentNode


def text_to_children(text):
    """
    Convert inline markdown text into a list of HTMLNode children.
    """
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def strip_code_fence(block):
    """Remove ``` fences from a code block."""
    if block.startswith("```") and block.endswith("```"):
        return block[3:-3].strip("\n")
    return block


def markdown_to_html_node(markdown):
    """
    Convert full markdown text into a single <div> ParentNode.
    Each block becomes a child HTML structure.
    """
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode("div", children=[])

    for block in blocks:
        btype = block_to_block_type(block)

        # --- HEADINGS ---
        if btype == BlockType.HEADING:
            m = re.match(r"^(#{1,6})\s+(.*)", block)
            if not m:
                continue
            level = len(m.group(1))
            text = m.group(2)
            children = text_to_children(text)
            node = ParentNode(f"h{level}", children)

        # --- PARAGRAPH ---
        elif btype == BlockType.PARAGRAPH:
            children = text_to_children(block)
            node = ParentNode("p", children)

        # --- CODE BLOCK ---
        elif btype == BlockType.CODE:
            code_text = strip_code_fence(block)
            code_node = text_node_to_html_node(TextNode(code_text, TextType.TEXT))
            pre = ParentNode("pre", [ParentNode("code", [code_node])])
            node = pre

        # --- QUOTE BLOCK ---
        elif btype == BlockType.QUOTE:
            lines = [re.sub(r"^>\s?", "", line) for line in block.splitlines()]
            quote_text = "\n".join(lines).strip()
            children = text_to_children(quote_text)
            node = ParentNode("blockquote", children)

        # --- UNORDERED LIST ---
        elif btype == BlockType.UNORDERED_LIST:
            items = []
            for line in block.splitlines():
                text = re.sub(r"^- ", "", line, count=1)
                li_children = text_to_children(text)
                items.append(ParentNode("li", li_children))
            node = ParentNode("ul", items)

        # --- ORDERED LIST ---
        elif btype == BlockType.ORDERED_LIST:
            items = []
            for line in block.splitlines():
                text = re.sub(r"^\d+\.\s+", "", line, count=1)
                li_children = text_to_children(text)
                items.append(ParentNode("li", li_children))
            node = ParentNode("ol", items)

        else:
            # fallback to paragraph
            node = ParentNode("p", text_to_children(block))

        parent.children.append(node)

    return parent

