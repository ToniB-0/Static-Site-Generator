# src/extract_title.py
import re

def extract_title(markdown: str) -> str:
    """
    Find the first H1 line in the markdown (a line that starts with a single '# '
    followed by the title text). Return the title text stripped of whitespace.
    If no H1 is found, raise a ValueError.
    """
    for line in markdown.splitlines():
        m = re.match(r'^#\s+(.*)', line)
        if m:
            return m.group(1).strip()
    raise ValueError("No H1 title found in markdown")

