from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from split_nodes_markdown import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    # Start with one plain text node
    nodes = [TextNode(text, TextType.TEXT)]

    # Apply delimiter splits
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # Apply image and link splits
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

