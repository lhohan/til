# Beads `bd query` defaults to 50 results

`bd query` shows only 50 issues by default.

Raise the limit (or set it to unlimited) with `--limit`:

```bash
bd query 'updated>2w' -a --limit 200
bd query 'updated>2w' -a --limit 0
```

_Created: 2026-02-26_
