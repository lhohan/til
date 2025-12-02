#!/usr/bin/env python3
"""
Prepare static site infrastructure for Zola.

This script handles Zola-specific setup tasks:
- Copies TIL markdown files from root topic directories to .work-dir/site/content/
- Injects TOML frontmatter during copy (extracts from H1 and footer metadata)
- Generates _index.md files for topics that don't have them

This runs before every build via the justfile to ensure the Zola site
has the correct structure.
"""

import sys
from pathlib import Path

# Add scripts directory to path for imports
SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from metadata_utils import get_metadata_for_file, inject_frontmatter


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


def get_topic_dirs() -> list[Path]:
    """Get all valid topic directories from root."""
    return [
        item for item in sorted(CONTENT_DIR.iterdir())
        if item.is_dir() and not item.name.startswith(".")
    ]


def ensure_topic_index(topic_dir: Path) -> bool:
    """Create _index.md for topic if it doesn't exist."""
    index_path = topic_dir / "_index.md"
    if index_path.exists():
        return False

    title = format_topic_title(topic_dir.name)
    index_path.write_text(TOPIC_INDEX_TEMPLATE.format(title=title))
    print(f"Created _index.md for {title}")
    return True


def copy_topic_files() -> None:
    """
    Copy TIL files from root to .work-dir/site/content/ with frontmatter injection.

    For each topic directory:
    - Copy markdown files to site/content/{topic}/
    - Extract metadata from H1 and footer
    - Inject TOML frontmatter for Zola
    """
    content_dest_dir = CONTENT_DIR / ".work-dir/site/content"
    content_dest_dir.mkdir(parents=True, exist_ok=True)

    # Track which files we've copied (to clean up orphans)
    copied_files = set()

    for topic_dir in get_topic_dirs():
        dest_dir = content_dest_dir / topic_dir.name
        dest_dir.mkdir(exist_ok=True)

        for md_file in topic_dir.glob("*.md"):
            # _index.md gets copied as-is (no transformation needed)
            if md_file.name == "_index.md":
                dest_file = dest_dir / md_file.name
                dest_file.write_text(md_file.read_text(encoding='utf-8'), encoding='utf-8')
                copied_files.add(dest_file)
                continue

            # Read plain markdown
            content = md_file.read_text(encoding='utf-8')

            # Extract metadata (H1, footer date, topic from path)
            metadata = get_metadata_for_file(md_file)

            # Inject frontmatter
            augmented_content = inject_frontmatter(content, metadata)

            # Write to destination
            dest_file = dest_dir / md_file.name
            dest_file.write_text(augmented_content, encoding='utf-8')
            copied_files.add(dest_file)

    # Clean up orphaned files (files in dest that no longer exist in source)
    # Skip special directories like 'search' that are managed separately
    for topic_dest_dir in content_dest_dir.iterdir():
        if not topic_dest_dir.is_dir() or topic_dest_dir.name.startswith("."):
            continue

        # Skip special directories (search, etc.)
        if topic_dest_dir.name in ("search",):
            continue

        for dest_file in topic_dest_dir.glob("*.md"):
            if dest_file not in copied_files:
                print(f"Removing orphaned file: {dest_file.relative_to(content_dest_dir)}")
                dest_file.unlink()


def main():
    """Prepare Zola site infrastructure."""
    # 1. Copy topic files with frontmatter injection
    copy_topic_files()

    # 2. Create _index.md files for all topics
    for item in get_topic_dirs():
        ensure_topic_index(item)


if __name__ == "__main__":
    main()
