import os
from pathlib import Path
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath="/"):
    """Generate a single HTML page from a markdown file."""
    print(f"Generating page from {from_path} → {dest_path} using {template_path}")

    # Read markdown
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    # Convert markdown → HTML
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    # Extract title from markdown
    title = extract_title(markdown)

    # Read template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Replace placeholders
    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_content)

    # Adjust href/src links based on basepath
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the final HTML file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Wrote: {dest_path}")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    """Recursively generate pages for all markdown files in the content directory."""
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(from_path):
            # Recurse into subdirectories
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
        elif os.path.isfile(from_path) and from_path.endswith(".md"):
            # Convert .md to .html
            new_dest = os.path.splitext(dest_path)[0] + ".html"
            generate_page(from_path, template_path, new_dest, basepath)

