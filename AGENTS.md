# CLAUDE.md

Guidance for LLM assistants working with this codebase.

## Quick Reference: Development Commands

```bash
just dev              # Start development server
just new-til <topic> <slug>  # Create new TIL entry
just build-content    # Prepare site (transform content + update README)
just build            # Full production build (includes search indexing)
just check            # Validate Zola configuration
just clean            # Remove generated output (.work-dir/site/public/)
```

## Project Overview

Personal knowledge base publishing TILs (Today I Learned) as:
1. Git-native markdown files in flat root-level topic directories
2. Static website at https://til.hanlho.com (built with Zola)

**Core content model contract**: Flat root-level topic directories with markdown files.

## Architecture Context

### Source Content Format

TIL markdown files use simple plain markdown format (located in root topic directories):

```markdown
# Your TIL Title

Content goes here...

_Created: YYYY-MM-DD_
```

- **H1 heading**: becomes the page title
- **Markdown body**: the TIL content
- **Footer pattern**: `_Created: YYYY-MM-DD_` provides publication date

### Build System

- **`.work-dir/site/prepare-site.py`**: Transforms source files (injects TOML frontmatter, strips H1/footer)
- **`.work-dir/site/content/`**: Transformed files ready for Zola (auto-created)
- **`.work-dir/site/templates/`**: Zola HTML templates
- **`.work-dir/site/config.toml`**: Zola configuration
- **`.work-dir/scripts/`**: Python utilities (new_til.py, update-readme.py, metadata_utils.py)

### Build Pipeline

The `just build-content` command orchestrates:
1. `prepare-site.py` - Copies files, extracts metadata, injects frontmatter
2. `update-readme.py` - Updates README TOC

Then `just dev` or `just build` runs Zola and optionally pagefind search indexing.

## For LLM Assistants: Additional Context

When working on build system changes:
- Read `.work-dir/agent_docs/README.md` for architecture overview
- For implementation details, read the source code directly (prepare-site.py, metadata_utils.py, etc.)

## Working with This Repository

**Before modifying build scripts or content transformation**:
1. Understand the pipeline: source (H1 + footer) → prepare-site.py (transforms) → Zola (generates)
2. Read relevant source code: `.work-dir/site/prepare-site.py`, `.work-dir/scripts/metadata_utils.py`
3. Test with `just dev` to verify changes work

**When creating new TILs**:
- Use `just new-til <topic> <slug>` (not manual file creation)
- This creates plain markdown with H1 and footer template
- Edit the file, then run `just build-content` to update README
- Verify with `just dev`

**When debugging build issues**:
- Run `just check` to validate Zola configuration
- Use `just clean` then rebuild if output seems stale
- Check `.work-dir/site/content/` to see transformed files
- Most issues are in prepare-site.py metadata extraction
