# `bookmark advance` Instead Of `tug` Aliases

`jj` has a new subcommand to manage bookmarks: `jj bookmark advance`.

Default behaviour is that it moves the closest bookmark to the working copy.

Before `bookmark advance`, I used `jj` aliases instead:

```
# Find the closest ancestor with a bookmark pointing at it, and move it to ...
# ...the working copy.
tug = ["bookmark", "move", "--from", "heads(::@- & bookmarks())", "--to", "@"]
# ...the parent of the working copy.
tug- = ["bookmark", "move", "--from", "heads(::@- & bookmarks())", "--to", "@-"]
```

In practice I only used `tug-` because the working copy cannot be pushed to a remote, and usually I update my bookmarks right before pushing.

## Issue

The default behaviour of `bookmark advance` is to move the closest bookmark to the working copy (`@`). I want to move the closest bookmark to the parent of the working copy (`@-`).

## Solution

To make `jj bookmark advance` move the closest bookmark to `@-`, in `.config/jj/config.toml` configure revsets:

```toml
[revsets]
bookmark-advance-from = 'heads(::to & bookmarks())'
bookmark-advance-to = '@-'
```

Verify:

```bash
jj config get revsets.bookmark-advance-from
jj config get revsets.bookmark-advance-to
```

Should output:

```text
heads(::to & bookmarks())
@-
```

_Created: 2026-09-23_
