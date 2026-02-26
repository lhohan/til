# Short way to set a Beads task in progress

The easiest way to put a Beads task in progress from the command line is to use the `claim` flag.

```bash
bd update --claim <id>
```

Note: `--claim` fails if the task is already assigned to someone else.

```text
Atomically claim the issue (sets assignee to you, status to in_progress; fails if already claimed)
```

_Created: 2026-02-26_
