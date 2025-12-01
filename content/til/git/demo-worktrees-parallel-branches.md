+++
title = "[DEMO] Git worktrees for parallel branches"
date = 2024-11-20
[taxonomies]
topics = ["git"]
+++

Git worktrees let you check out multiple branches simultaneously in separate directories without cloning the repo multiple times.

```bash
# Create a worktree for a feature branch
git worktree add ../feature-branch feature-branch

# List all worktrees
git worktree list

# Remove a worktree when done
git worktree remove ../feature-branch
```

This is perfect for:
- Reviewing PRs while keeping your work intact
- Running tests on one branch while developing on another
- Comparing behavior across branches side-by-side

Each worktree shares the same `.git` directory, so they're lightweight and stay in sync.
