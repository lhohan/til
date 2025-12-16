# Swapping Two Commits

To swap 2 commits (assuming you are on the top commit):

```
❯ jj rebase -r @- -d @ && jj new @+
```

Now you are on a new commit on top of the swapped commit.

jj rebase` moves the parent commit to become a child, then `jj new` creates a new working commit on top.

## Example

```bash
❯ jj log
@  lzpkwyqm feat(til): TIL rules to remember main* 13 minutes ago
○  pksmqlqx chore(llm): Add TIL rules checker agent git_head() 13 minutes ago
◆  ltsxsqxy feat(til): Add using home manager to manage llm-agents 3 hours ago
```

```bash
❯ jj rebase -r @- -d @ && jj new @+
Rebased 1 commits onto destination
Rebased 1 descendant commits
Working copy  (@) now at: lzpkwyqm 2fede003 main* | feat(til): TIL rules to remember
Parent commit (@-)      : ltsxsqxy 03e9d86e feat(til): Add using home manager to manage llm-agents
Added 0 files, modified 0 files, removed 1 files
Working copy  (@) now at: zwlpyvry d6fb4a95 (empty) (no description set)
Parent commit (@-)      : pksmqlqx d4b0ccba chore(llm): Add TIL rules checker agent
Added 1 files, modified 0 files, removed 0 files
```

```bash
❯ jj log
@  zwlpyvry (empty) (no description set) 2 seconds ago
○  pksmqlqx chore(llm): Add TIL rules checker agent git_head() 2 seconds ago
○  lzpkwyqm feat(til): TIL rules to remember main* 2 seconds ago
◆  ltsxsqxy feat(til): Add using home manager to manage llm-agents 3 hours ago
```

_Created: 2025-12-16_
