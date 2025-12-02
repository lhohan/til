#!/usr/bin/env python3
"""Utility for creating new TIL markdown entries."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new TIL entry")
    parser.add_argument("topic", help="Directory (topic) to place the entry under")
    parser.add_argument("slug", help="File slug (lowercase, digits, hyphens)")
    return parser.parse_args()


def ensure_valid_slug(slug: str) -> None:
    if not re.fullmatch(r"[a-z0-9-]+", slug):
        raise ValueError(
            "Slug must contain only lowercase letters, digits, and hyphens (e.g. git-aliases)."
        )


def derive_title(slug: str) -> str:
    return slug.replace("-", " ").title()


def create_entry(topic: str, slug: str) -> Path:
    ensure_valid_slug(slug)

    topic_dir = (REPO_ROOT / topic).resolve()
    topic_dir.mkdir(parents=True, exist_ok=True)

    target_file = topic_dir / f"{slug}.md"
    if target_file.exists():
        raise FileExistsError(f"Entry already exists: {target_file}")

    title = derive_title(slug)
    today = date.today().isoformat()

    # Create plain markdown with H1 and footer
    content = f"""# {title}

Describe what you learned here.

_Created: {today}_
"""

    target_file.write_text(content, encoding="utf-8")
    return target_file


def main() -> int:
    args = parse_args()
    try:
        created_path = create_entry(args.topic, args.slug)
    except (ValueError, FileExistsError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Created {created_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
