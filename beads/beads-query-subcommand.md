# Beads has a dedicated `query` subcommand

I wanted to find all tasks I worked on in the last 2 weeks.
Beads also a `query` subcommand that can express these kind of filters (instead of `bd list`).

To get _all_ issues worked on in the past 2 weeks:

```bash
bd query 'updated>2w' -a --limit 0
```

For more info:

```bash
bd query --help
```


_Created: 2026-02-26_
