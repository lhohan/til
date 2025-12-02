# CLAUDE.md

This file provides guidance to LLM's like Claude Code (claude.ai/code) when working with code in this repository.

## Version Control

This repository uses **Jujutsu (jj)**, not git. Always use `jj` commands for version control operations.

## Development Commands

```bash
# Start local development server (builds content + serves with Zola)
just dev

# Create new TIL entry
just new-til <topic> <slug>
# Example: just new-til python my-learning

# Update README TOC and prepare Zola site structure
just build-content

# Production build (includes pagefind search indexing)
just build

# Check Zola configuration and content
just check
```

## Repository Architecture

This is a personal knowledge base that publishes TILs (Today I Learned) both as:
1. Git-native markdown files organized by topic directories
2. A static website at https://til.hanlho.com built with Zola

### Content Structure

- **Topic directories** (root level)
  - Each contains TIL markdown files
  - Each has an `_index.md` for topic metadata
  - TIL files have TOML frontmatter with title, date, and topics taxonomy

- **`.work-dir/site/`**: Zola static site generator
  - `content/`: Symlinks to root topic directories (auto-created by prepare-site.py)
  - `templates/`: Zola HTML templates
  - `config.toml`: Zola configuration

- **`.work-dir/scripts/`**: Python automation utilities

### Build Process Flow

```
1. prepare-site.py
   ├─ Creates symlinks in .work-dir/site/content/ → root topic dirs
   └─ Generates _index.md files for each topic

2. update-readme.py
   └─ Scans TILs and updates README TOC (between <!-- TOC START/END --> markers)

3. zola build
   └─ Generates static site in .work-dir/site/public/

4. pagefind (production only)
   └─ Indexes site for full-text search
```

The `just build-content` command runs steps 1-2. The `just dev` command runs build-content then serves with Zola. The `just build` command runs all steps for production.

## Creating New TILs

Use `just new-til <topic> <slug>` which:
- Creates a new markdown file at `<topic>/<slug>.md`
- Auto-generates TOML frontmatter with title (derived from slug), date, and topics taxonomy
- Validates slug format (lowercase letters, digits, hyphens only)

TIL frontmatter format:
```toml
+++
title = "Title Here"
date = YYYY-MM-DD
[taxonomies]
topics = ["topic-name"]
+++
```

After creating a TIL, run `just build-content` to update the README TOC and prepare the Zola site structure.

## Deployment

GitHub Actions workflow (`.github/workflows/deploy.yml`) automatically:
1. Updates README TOC
2. Builds site with Zola
3. Deploys to VPS via rsync

Triggers on push to `main` branch affecting TIL content or site configuration.
