#!/usr/bin/env python3
"""
Shared utilities for extracting and injecting TIL metadata.

This module provides functions to parse metadata from plain markdown files
(H1 titles, footer dates) and inject TOML frontmatter for Zola.
"""

from __future__ import annotations

import re
from pathlib import Path


def extract_h1_title(content: str) -> str | None:
    """
    Extract the first H1 heading from markdown content.

    Args:
        content: Markdown file content

    Returns:
        The H1 text (without the # prefix) or None if not found
    """
    match = re.search(r'^# (.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else None


def extract_footer_date(content: str) -> str | None:
    """
    Extract date from footer pattern: _Created: YYYY-MM-DD_

    Args:
        content: Markdown file content

    Returns:
        The date string in ISO format (YYYY-MM-DD) or None if not found
    """
    match = re.search(r'_Created: (\d{4}-\d{2}-\d{2})_', content)
    return match.group(1) if match else None


def extract_topic_from_path(file_path: Path) -> str:
    """
    Get the topic name from the file's parent directory.

    Args:
        file_path: Path to the markdown file

    Returns:
        The parent directory name (topic)
    """
    return file_path.parent.name


def inject_frontmatter(content: str, metadata: dict) -> str:
    """
    Prepend TOML frontmatter to markdown content and strip H1 title and footer date.

    Args:
        content: Plain markdown content
        metadata: Dict with 'title', 'date', and 'topics' keys

    Returns:
        Content with TOML frontmatter prepended and H1/footer removed
    """
    title = metadata.get('title', 'Untitled')
    date = metadata.get('date', '2025-01-01')
    topics = metadata.get('topics', [])

    # Strip H1 title from content (first line that starts with #)
    content = re.sub(r'^# .+$\n*', '', content, count=1, flags=re.MULTILINE)

    # Strip footer date from content (_Created: YYYY-MM-DD_)
    content = re.sub(r'\n*_Created: \d{4}-\d{2}-\d{2}_\s*$', '', content)

    # Format topics array for TOML
    topics_str = ', '.join(f'"{topic}"' for topic in topics)

    frontmatter = f"""+++
title = "{title}"
date = {date}
[taxonomies]
topics = [{topics_str}]
+++

"""

    return frontmatter + content.lstrip()


def parse_existing_frontmatter(content: str) -> tuple[dict, str]:
    """
    Parse existing TOML frontmatter from markdown (for backward compatibility).

    Args:
        content: Markdown content that may have TOML frontmatter

    Returns:
        Tuple of (metadata_dict, content_without_frontmatter)
        Returns ({}, content) if no frontmatter found
    """
    match = re.match(r'^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n', content, re.DOTALL)

    if not match:
        return {}, content

    frontmatter_text = match.group(1)
    body = content[match.end():]

    # Parse simple TOML frontmatter
    metadata = {}
    for line in frontmatter_text.split('\n'):
        if '=' in line and not line.strip().startswith('['):
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"')
            metadata[key] = value

    return metadata, body


def get_metadata_for_file(file_path: Path) -> dict:
    """
    Smart metadata extraction: tries plain markdown format first,
    falls back to frontmatter parsing for backward compatibility.

    Args:
        file_path: Path to the markdown file

    Returns:
        Dict with 'title', 'date', and 'topics' keys
    """
    content = file_path.read_text(encoding='utf-8')

    # Try plain markdown format
    title = extract_h1_title(content)
    date = extract_footer_date(content)
    topic = extract_topic_from_path(file_path)

    # Fallback to frontmatter if plain markdown missing
    if not title or not date:
        fm, _ = parse_existing_frontmatter(content)
        title = title or fm.get('title', file_path.stem)
        date = date or fm.get('date', '2025-01-01')

    return {
        'title': title,
        'date': date,
        'topics': [topic]
    }
