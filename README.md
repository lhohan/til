# Today I Learned

A collection of concise write-ups on small things I learn day to day across various topics.

Inspired by [Simon Willison's TIL](https://til.simonwillison.net/). Built with [Zola](https://www.getzola.org/).

## Table of Contents

<!-- TOC START -->
**8 TILs** across **4 topics**


### Git

- [[DEMO] Git worktrees for parallel branches](content/til/git/demo-worktrees-parallel-branches.md)
- [[DEMO] Interactive rebase with autosquash](content/til/git/demo-interactive-rebase-autosquash.md)

### Python

- [[DEMO] Prefer pathlib over os.path](content/til/python/demo-pathlib-over-os-path.md)
- [[DEMO] The walrus operator for assignment expressions](content/til/python/demo-walrus-operator.md)

### Rust

- [[DEMO] Auto-reload with cargo-watch](content/til/rust/demo-cargo-watch-reload.md)
- [[DEMO] Option::map vs Option::and_then](content/til/rust/demo-option-map-vs-and-then.md)

### Zola

- [[DEMO] Shortcodes for reusable embeds](content/til/zola/demo-shortcodes-for-embeds.md)
- [[DEMO] Taxonomies for organizing content](content/til/zola/demo-taxonomies-for-tags.md)
<!-- TOC END -->

## Development

This project uses Nix flakes for reproducible development environment.

```bash
# Enter dev shell (requires Nix with flakes)
nix develop

# Or with direnv
direnv allow

# Start dev server
just dev

# Build site
just build

# Update README TOC
just update-readme
```

## Deployment

Deployed via GitHub Actions to Hetzner VPS using rsync over SSH.

Required secrets:
- `VPS_HOST` - Server hostname or IP
- `VPS_USER` - SSH username
- `VPS_SSH_KEY` - Private SSH key (ed25519)
- `VPS_PATH` - Deployment path on server (e.g., `/var/www/til`)

## Adding a TIL

1. Create a new markdown file in `content/til/<topic>/`
2. Add frontmatter:

```toml
+++
title = "Your TIL title"
date = 2024-01-15
[taxonomies]
topics = ["topic-name"]
+++
```

3. Write your content
4. Commit and push - the README TOC updates automatically

## License

MIT
