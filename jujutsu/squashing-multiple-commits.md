# Squashing Multiple Commits

`jj` makes it easy to create intermediate commits as save points, then squash them into a single commit when finished.

After creating several commits, use `jj squash` to combine them:

```bash
# Squash a range of commits into a target commit
# '<commit-1>' is the value of the start commit of the range
# '<commit-2>' is the value of the destingatio commit
❯ jj squash --from <commit-1>::@ --into <commit-2> -m "feat xyz"

# Alternatively, use relative references (e.g., 3rd parent)
❯ jj squash --from @---::@ --into <commit-2> -m "feat xyz"
```

- `--from` specifies the commit or range to squash.
- `--into` specifies the target commit.
- `-m` sets the new commit message. Omit if you want a text editor.

Verifying the result:

```bash
❯ jj show @- --no-pager
feat xyz

Added regular file ...
...
```

If you make a mistake with commit references, `jj undo` easily reverts the squash.

_Created: 2025-12-20_
