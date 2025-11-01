import re
from block_type import BlockType

def block_to_block_type(block: str) -> BlockType:
    """Classify a block of markdown text into its BlockType."""
    lines = block.strip().split("\n")

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(re.match(r"^- ", line) for line in lines):
        return BlockType.UNORDERED_LIST

    if all(re.match(r"^\d+\. ", line) for line in lines):
        numbers = [int(line.split(".")[0]) for line in lines]
        if numbers == list(range(1, len(lines) + 1)):
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

