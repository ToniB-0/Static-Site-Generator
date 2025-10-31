import os
from pathlib import Path
from markdown_to_html_node import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    from main import extract_title
    """
    Recursively generate HTML pages from markdown files in content directory.

    Args:
        dir_path_content: path to the content folder (source markdown files)
        template_path: path to template.html
        dest_dir_path: destination public directory
    """
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(entry_path):
            # Create matching directory in destination
            Path(dest_path).mkdir(parents=True, exist_ok=True)
            # Recurse into subdirectory
            generate_pages_recursive(entry_path, template_path, dest_path)
        elif os.path.isfile(entry_path) and entry.lower().endswith(".md"):
            # Generate the HTML file
            html_filename = os.path.splitext(entry)[0] + ".html"
            dest_file_path = os.path.join(dest_dir_path, html_filename)

            print(f"Generating page: {entry_path} -> {dest_file_path}")

            with open(entry_path, "r", encoding="utf-8") as f:
                markdown_content = f.read()
            with open(template_path, "r", encoding="utf-8") as f:
                template_content = f.read()

            html_content = markdown_to_html_node(markdown_content).to_html()
            title = extract_title(markdown_content)

            final_html = template_content.replace("{{ Title }}", title)
            final_html = final_html.replace("{{ Content }}", html_content)

            # Write HTML file
            with open(dest_file_path, "w", encoding="utf-8") as f:
                f.write(final_html)

