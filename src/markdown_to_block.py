def markdown_to_blocks(markdown):
    # Split on two or more newlines
    raw_blocks = markdown.split("\n\n")

    # Clean and remove empty ones
    blocks = [block.strip() for block in raw_blocks if block.strip() != ""]

    return blocks

