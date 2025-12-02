#!/usr/bin/env python3
"""
Prepare static site infrastructure for Zola.

This script handles Zola-specific setup tasks:
- Creates symlinks in .work-dir/site/content/ pointing to root topic directories
- Generates _index.md files for topics that don't have them

This runs before every build via the justfile to ensure the Zola site
has the correct structure.
"""

from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent.parent

TOPIC_INDEX_TEMPLATE = """+++
title = "{title}"
sort_by = "date"
template = "section.html"
page_template = "page.html"
transparent = true
+++\n"""


def format_topic_title(name: str) -> str:
    """Convert topic directory name to title case."""
    return name.replace("-", " ").title()


def ensure_topic_index(topic_dir: Path) -> bool:
    """Create _index.md for topic if it doesn't exist."""
    index_path = topic_dir / "_index.md"
    if index_path.exists():
        return False

    title = format_topic_title(topic_dir.name)
    index_path.write_text(TOPIC_INDEX_TEMPLATE.format(title=title))
    print(f"Created _index.md for {title}")
    return True


def ensure_topic_symlinks() -> None:
    """Create symlinks in .work-dir/site/content/ for all topic directories."""
    content_symlink_dir = CONTENT_DIR / ".work-dir/site/content"

    # Ensure the content directory exists
    content_symlink_dir.mkdir(parents=True, exist_ok=True)

    # Get all valid topic directories from root
    for item in sorted(CONTENT_DIR.iterdir()):
        if not item.is_dir() or item.name.startswith("."):
            continue

        topic_name = item.name
        symlink_path = content_symlink_dir / topic_name

        # Create symlink if it doesn't exist
        if not symlink_path.exists():
            target = Path(f"../../../{topic_name}")
            try:
                symlink_path.symlink_to(target)
                print(f"Created symlink: {topic_name}")
            except OSError as e:
                print(f"Warning: Could not create symlink for {topic_name}: {e}")


def main():
    """Prepare Zola site infrastructure."""
    # 1. Create symlinks first
    ensure_topic_symlinks()

    # 2. Create _index.md files for all topics
    for item in sorted(CONTENT_DIR.iterdir()):
        if not item.is_dir() or item.name.startswith("."):
            continue
        ensure_topic_index(item)


if __name__ == "__main__":
    main()
