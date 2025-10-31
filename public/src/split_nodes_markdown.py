from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_images(text)

        if not matches:
            new_nodes.append(node)
            continue

        split_nodes = []
        for alt, url in matches:
            before, sep, after = text.partition(f"![{alt}]({url})")
            if before:
                split_nodes.append(TextNode(before, TextType.TEXT))
            split_nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = after  # move forward

        if text:
            split_nodes.append(TextNode(text, TextType.TEXT))

        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_links(text)

        if not matches:
            new_nodes.append(node)
            continue

        split_nodes = []
        for alt, url in matches:
            before, sep, after = text.partition(f"[{alt}]({url})")
            if before:
                split_nodes.append(TextNode(before, TextType.TEXT))
            split_nodes.append(TextNode(alt, TextType.LINK, url))
            text = after

        if text:
            split_nodes.append(TextNode(text, TextType.TEXT))

        new_nodes.extend(split_nodes)
    return new_nodes

