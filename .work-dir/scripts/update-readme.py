#!/usr/bin/env python3
"""
Scan TIL content and update README.md with a table of contents.

This script:
- Scans all topic directories at the root level
- Extracts metadata (title, date) from markdown file frontmatter
- Generates a TOC sorted by topic and date
- Injects the TOC between <!-- TOC START --> and <!-- TOC END --> markers in README.md

This runs as part of the build process to keep the README in sync with TIL content.
"""

import re
from collections import defaultdict
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent.parent
README_PATH = Path(__file__).parent.parent.parent / "README.md"

TOC_START = "<!-- TOC START -->"
TOC_END = "<!-- TOC END -->"


def extract_frontmatter(content: str) -> dict:
    """Extract TOML frontmatter from markdown file."""
    match = re.match(r"^\+\+\+\s*\n(.*?)\n\+\+\+", content, re.DOTALL)
    if not match:
        return {}

    fm = {}
    for line in match.group(1).split("\n"):
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"')
            fm[key] = value
    return fm


def get_tils() -> dict[str, list[tuple[str, str, str]]]:
    """
    Scan content directory and return TILs grouped by topic.
    Returns: {topic: [(title, date, relative_path), ...]}
    """
    tils = defaultdict(list)

    for item in sorted(CONTENT_DIR.iterdir()):
        if not item.is_dir() or item.name.startswith("."):
            continue

        topic_dir = item
        topic = topic_dir.name

        for md_file in sorted(topic_dir.glob("*.md")):
            if md_file.name == "_index.md":
                continue
            content = md_file.read_text()
            fm = extract_frontmatter(content)

            title = fm.get("title", md_file.stem)
            date = fm.get("date", "")
            rel_path = md_file.relative_to(CONTENT_DIR)

            tils[topic].append((title, date, str(rel_path)))

    return dict(tils)


def generate_toc(tils: dict) -> str:
    """Generate markdown TOC from TILs dict."""
    lines = []
    total = sum(len(items) for items in tils.values())
    lines.append(f"**{total} TILs** across **{len(tils)} topics**\n")

    for topic in sorted(tils.keys()):
        lines.append(f"\n### {topic.title()}\n")
        for title, date, path in sorted(tils[topic], key=lambda x: x[1], reverse=True):
            lines.append(f"- [{title}]({path})")

    return "\n".join(lines)


def update_readme(toc: str) -> bool:
    """Update README.md with new TOC. Returns True if changed."""
    if not README_PATH.exists():
        print(f"README.md not found at {README_PATH}")
        return False

    content = README_PATH.read_text()

    if TOC_START not in content or TOC_END not in content:
        print(f"TOC markers not found in README.md")
        return False

    pattern = re.compile(
        rf"({re.escape(TOC_START)})\n.*?\n({re.escape(TOC_END)})", re.DOTALL
    )

    new_content = pattern.sub(rf"\1\n{toc}\n\2", content)

    if new_content == content:
        print("README.md already up to date")
        return False

    README_PATH.write_text(new_content)
    print("README.md updated")
    return True


def main():
    tils = get_tils()
    if not tils:
        print("No TILs found")
        return

    toc = generate_toc(tils)
    update_readme(toc)


if __name__ == "__main__":
    main()
