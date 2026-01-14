# Ignoring A Tracked File

To remove a file from the `jj` working copy:

```bash
❯ ls
file.db

❯ jj st --no-pager .
Working copy changes:
A file.db
Working copy  (@) : xzktruuo 94d90aa8 (no description set)
...

❯ jj file untrack file.db
Error: 'file.db' is not ignored.
Hint: Files that are not ignored will be added back by the next command.
Make sure they're ignored, then try again.
```

Always to see the creators thought of putting a helpful error message.

```bash
❯ echo file.db >> .gitignore
❯ jj file untrack file.db

❯ jj st --no-pager .
Working copy changes:
A .gitignore
Working copy  (@) : xzktruuo d62385e7 (no description set)
...

❯ ls
file.db
```


_Created: 2026-01-14_
