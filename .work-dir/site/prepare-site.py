#!/usr/bin/env python3
"""
Prepare static site infrastructure for Zola.

This script handles Zola-specific setup tasks:
- Copies TIL markdown files from root topic directories to .work-dir/site/content/
- Injects TOML frontmatter during copy (extracts from H1 and footer metadata)
- Recursively copies all non-markdown files (images, PDFs, etc.) to .work-dir/site/static/
- Generates _index.md files for topics that don't have them

This runs before every build via the justfile to ensure the Zola site
has the correct structure.
"""

import shutil
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
        item
        for item in sorted(CONTENT_DIR.iterdir())
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
    - Copy markdown files to site/content/{topic}/ with TOML frontmatter injection
    - Recursively copy all non-markdown files to site/static/{topic}/ maintaining directory structure
    - Extract metadata from H1 and footer for markdown files
    """
    content_dest_dir = CONTENT_DIR / ".work-dir/site/content"
    static_dest_dir = CONTENT_DIR / ".work-dir/site/static"
    content_dest_dir.mkdir(parents=True, exist_ok=True)
    static_dest_dir.mkdir(parents=True, exist_ok=True)

    # Track which items we've copied (to clean up orphans)
    copied_content_items = set()
    copied_static_items = set()

    for topic_dir in get_topic_dirs():
        content_topic_dir = content_dest_dir / topic_dir.name
        static_topic_dir = static_dest_dir / topic_dir.name
        content_topic_dir.mkdir(exist_ok=True)

        # Process all files and directories recursively
        for item in topic_dir.rglob("*"):
            # Skip hidden files/directories
            if any(part.startswith(".") for part in item.parts):
                continue

            # Calculate relative path from topic directory
            rel_path = item.relative_to(topic_dir)

            # Handle directories
            if item.is_dir():
                # Create in both content and static (will be used as needed)
                content_dir = content_topic_dir / rel_path
                static_dir = static_topic_dir / rel_path
                content_dir.mkdir(parents=True, exist_ok=True)
                static_dir.mkdir(parents=True, exist_ok=True)
                copied_content_items.add(content_dir)
                copied_static_items.add(static_dir)
                continue

            # Handle markdown files (with frontmatter injection) -> go to content/
            if item.suffix == ".md":
                dest_item = content_topic_dir / rel_path

                # _index.md gets copied as-is (no transformation needed)
                if item.name == "_index.md":
                    dest_item.parent.mkdir(parents=True, exist_ok=True)
                    dest_item.write_text(
                        item.read_text(encoding="utf-8"), encoding="utf-8"
                    )
                    copied_content_items.add(dest_item)
                    continue

                # Read plain markdown
                content = item.read_text(encoding="utf-8")

                # Extract metadata (H1, footer date, topic from path)
                metadata = get_metadata_for_file(item)

                # Inject frontmatter
                augmented_content = inject_frontmatter(content, metadata)

                # Write to destination
                dest_item.parent.mkdir(parents=True, exist_ok=True)
                dest_item.write_text(augmented_content, encoding="utf-8")
                copied_content_items.add(dest_item)
            else:
                # Copy non-markdown files to static/ (images, PDFs, etc.)
                dest_item = static_topic_dir / rel_path
                dest_item.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest_item)
                copied_static_items.add(dest_item)
                print(f"  Copied asset: {topic_dir.name}/{rel_path}")

    # Clean up orphaned files in content/
    for topic_dest_dir in content_dest_dir.iterdir():
        if not topic_dest_dir.is_dir() or topic_dest_dir.name.startswith("."):
            continue
        if topic_dest_dir.name in ("search",):
            continue

        for dest_item in topic_dest_dir.rglob("*"):
            if dest_item.is_file() and dest_item not in copied_content_items:
                print(
                    f"Removing orphaned file: {dest_item.relative_to(content_dest_dir)}"
                )
                dest_item.unlink()

        for dest_item in sorted(topic_dest_dir.rglob("*"), reverse=True):
            if dest_item.is_dir() and not any(dest_item.iterdir()):
                if dest_item not in copied_content_items:
                    print(
                        f"Removing empty directory: {dest_item.relative_to(content_dest_dir)}"
                    )
                    dest_item.rmdir()

    # Clean up orphaned files in static/
    for topic_dest_dir in static_dest_dir.iterdir():
        if not topic_dest_dir.is_dir() or topic_dest_dir.name.startswith("."):
            continue
        # Skip existing static assets (css, etc.)
        if topic_dest_dir.name in ("css", "manifest.json", "robots.txt", "favicon.svg"):
            continue

        for dest_item in topic_dest_dir.rglob("*"):
            if dest_item.is_file() and dest_item not in copied_static_items:
                print(
                    f"Removing orphaned static file: {dest_item.relative_to(static_dest_dir)}"
                )
                dest_item.unlink()

        for dest_item in sorted(topic_dest_dir.rglob("*"), reverse=True):
            if dest_item.is_dir() and not any(dest_item.iterdir()):
                if dest_item not in copied_static_items:
                    print(
                        f"Removing empty static directory: {dest_item.relative_to(static_dest_dir)}"
                    )
                    dest_item.rmdir()


def main():
    """Prepare Zola site infrastructure."""
    # 1. Copy topic files with frontmatter injection
    copy_topic_files()

    # 2. Create _index.md files for all topics
    for item in get_topic_dirs():
        ensure_topic_index(item)


if __name__ == "__main__":
    main()
