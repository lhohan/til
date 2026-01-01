# Show All Open Work

To get all open work, add to `jj`s `config.toml`:

```toml
open = ["log", "-r", "((mutable() & bookmarks(main)) | (bookmarks() ~ trunk())) | bookmarks(main)"]
```

then run

```bash
jj open
```

This will give all unpushed mutable commits on `main`, non-merged bookmarks and the main bookmark commit as a reference anchor for the tree visualization.

## Explanation

`jj` supports [a functional language for selecting a set of revisions](https://docs.jj-vcs.dev/latest/revsets/): 

- `bookmarks(main)`: The commit with the `main` bookmark.
- `mutable()`: Selects commits that are both mutable and the `main` bookmark.
- `bookmarks() ~ trunk()`: All bookmarks that haven't been merged to the `main` yet.
  - `bookmarks()` - Returns all commits that have any bookmark pointing to them.
  - `trunk()` - Returns the main/default branch commit (typically the latest commit on the remote main branch).
  - `~` (difference operator) - Subtracts the second set from the first, so this selects bookmarks that are NOT at trunk.
- `... | bookmarks(main)`: Include the commit with the `main` bookmark as a reference point.
  

_Created: 2025-12-21_
