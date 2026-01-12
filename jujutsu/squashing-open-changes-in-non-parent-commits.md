# Squashing Open Changes into Non-Parent Commits

Sometimes I end up with uncommitted changes in my working copy that logically belong to an earlier commit rather than the most recent one (or even further back in history).

For example, this happens to me more often than I care to admit: I forget to commit deleted files when moving them between directories. By the time I notice, I've already made another commit, and the deletions should have been part of the earlier move commit.

To squash changes from your working copy into (for example) the commit before the last commit:

```bash
jj squash --into @--
```

_Created: 2026-01-12_
