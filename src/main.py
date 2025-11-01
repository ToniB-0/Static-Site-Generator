import os
import sys
from generate_pages_recursive import generate_pages_recursive


def extract_title(markdown: str) -> str:
    """Extract the H1 title from markdown (first line starting with # )."""
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# ") and not line.startswith("##"):
            return line[2:].strip()
    raise ValueError("No H1 header found in markdown.")


# ------------------ Static Copy Functions ------------------

def copy_static_to_public(static_dir, public_dir):
    if os.path.exists(public_dir):
        delete_dir(public_dir)
    os.mkdir(public_dir)
    copy_dir_contents(static_dir, public_dir)


def delete_dir(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            delete_dir(full_path)
        else:
            os.remove(full_path)
    os.rmdir(path)


def copy_dir_contents(src, dest):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        if os.path.isdir(src_path):
            os.mkdir(dest_path)
            copy_dir_contents(src_path, dest_path)
        else:
            with open(src_path, "rb") as fsrc:
                data = fsrc.read()
            with open(dest_path, "wb") as fdest:
                fdest.write(data)


# ------------------ Main Build ------------------

def main():
    # Handle basepath CLI argument (for GitHub Pages)
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    root = os.path.dirname(__file__)
    static_dir = os.path.join(root, "..", "static")
    content_dir = os.path.join(root, "..", "content")
    template_path = os.path.join(root, "..", "template.html")
    docs_dir = os.path.join(root, "..", "docs")  # GitHub Pages target directory

    print(f"Base path: {basepath}")

    # Copy static assets
    print("Copying static files...")
    copy_static_to_public(static_dir, docs_dir)

    # Generate pages recursively
    print("Generating pages...")
    generate_pages_recursive(content_dir, template_path, docs_dir, basepath)

    print("✅ Site generation complete!")


if __name__ == "__main__":
    main()

