# Architecture Overview

This directory contains supplementary documentation for the TIL repository build system. For implementation details, read the source code directly.

## System Architecture

**Source → Transform → Build → Deploy**

1. **Source**: Plain markdown files in root topic directories
   - Format: H1 heading + markdown body + footer date (`_Created: YYYY-MM-DD_`)
   - Location: `<topic>/filename.md`

2. **Transform** (`.work-dir/site/prepare-site.py`):
   - Copies files to `.work-dir/site/content/`
   - Extracts metadata (title, date, topic)
   - Injects TOML frontmatter for Zola
   - Strips H1 and footer from content

3. **Build** (Zola):
   - Reads transformed markdown in `.work-dir/site/content/`
   - Generates HTML static site to `.work-dir/site/public/`
   - Uses templates in `.work-dir/site/templates/`

4. **Index** (Pagefind - production only):
   - Creates full-text search index
   - Only runs in `just build` (not dev)

## Key Concepts

**Content Model Contract**: Flat root-level topic directories with markdown files. Don't nest topics.

**Metadata Extraction**: `metadata_utils.py` uses smart extraction:
- Tries H1 + footer format first (current)
- Falls back to TOML frontmatter parsing (backward compatibility)
- Derives topic from directory name

**Build Orchestration**: `justfile` runs:
- `just build-content` → prepare-site.py + update-readme.py
- `just dev` → build-content + zola serve
- `just build` → build-content + zola build + pagefind

## When to Read the Code

Read the source code directly for:
- `prepare-site.py`: How metadata is extracted and transformed
- `metadata_utils.py`: Specific regex patterns and extraction logic
- `update-readme.py`: How README TOC is generated
- `new_til.py`: How new TILs are created
- `.work-dir/site/config.toml`: Zola configuration
- `.work-dir/site/templates/*.html`: How pages are rendered

## Maintenance

When the system changes:
1. Update source code (prepare-site.py, etc.)
2. Update AGENTS.md only if command syntax or workflow changes
3. Don't maintain separate documentation of code behavior - the code is the source of truth
4. If someone needs to understand how something works, point them to read the code

## Creating New TILs

```bash
just new-til <topic> <slug>    # Creates <topic>/<slug>.md
# Edit the file
just build-content              # Updates README + prepares site
just dev                        # Verify in local server
```

## Common Workflows

**Local development**:
```bash
just dev                        # Starts http://localhost:1111
# Edit markdown files, browser auto-refreshes
```

**Production build**:
```bash
just build                      # Full build with search indexing
```

**Verify configuration**:
```bash
just check                      # Validates Zola setup
```

**Clean up**:
```bash
just clean                      # Removes .work-dir/site/public/
```
