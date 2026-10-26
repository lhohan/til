# Excluding Paths From Commit

To commit everything in the working copy except one path, negate it with `~` instead of listing every path you want to include:

```
❯ jj
Working copy changes:
M .gitignore
D .scalafmt.conf
D script/project.scala
A docs/plans/2026-10-26-rust-migration.md
```

```bash
jj commit -m "refactor: remove Scala remnants after Rust migration" ~docs/
```

This commits the Scala removal and leaves the plan document in the working copy.

- `~x` is a fileset expression meaning "everything except `x`".
- Negations combine with inclusions: `jj commit -m "..." src/ ~src/generated/`.

Reference: [filesets](https://docs.jj-vcs.dev/latest/filesets/)

_Created: 2026-10-26_
