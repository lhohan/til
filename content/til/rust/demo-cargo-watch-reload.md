+++
title = "[DEMO] Auto-reload with cargo-watch"
date = 2024-11-25
[taxonomies]
topics = ["rust"]
+++

`cargo-watch` automatically re-runs commands when source files change, similar to nodemon for Node.js.

```bash
# Install
cargo install cargo-watch

# Run tests on every save
cargo watch -x test

# Check and run
cargo watch -x check -x run

# Clear screen between runs
cargo watch -c -x run

# Ignore specific paths
cargo watch -i "*.txt" -x run
```

For web development, combine with `-w` to watch specific directories:

```bash
cargo watch -w src -w templates -x run
```

This dramatically speeds up the development feedback loop.
