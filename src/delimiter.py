from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Skip non-text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # Split the text on the delimiter
        parts = node.text.split(delimiter)

        # If even number of parts → unmatched delimiter
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in: {node.text}")

        # Build a list of new subnodes
        split_nodes = []
        for i, part in enumerate(parts):
            if not part:
                continue  # skip empty segments
            if i % 2 == 0:
                split_nodes.append(TextNode(part, TextType.TEXT))
            else:
                split_nodes.append(TextNode(part, text_type))

        # Add them all at once
        new_nodes.extend(split_nodes)

    return new_nodes    
