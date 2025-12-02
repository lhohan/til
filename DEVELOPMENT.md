# Development

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

# Update README TOC + prepare Zola site
just build-content
```

## Tooling website

Alongside this TIL repo a static site is also deployed at [Hanlho TILs](https://til.hanlho.com), this site is built with [Zola](https://www.getzola.org/). Current implementation is supported by scripts to link all content together. See the `.work-dir/site/prepare-site.py` script. To run typically use `just build-content`.

The site is managed in `.work-dir/site`.
