# Rebasing A Remote Bookmark

When you fetch a remote bookmark (git branch) using `jj` at some point you may want to rebase it on main. The flow is as follows:

1. Track the remote bookmark to make it mutable:

```bash
❯ jj bookmark track feature-xyz@origin
```

2. Rebase the hash reference onto `main`:

```bash
❯ jj rebase -r kw -d main
```

3. Move the `main` bookmark (assuming you the rebased commit is now on `@-`, otherwise use the appropriate ref):

```bash
jj bookmark set main -r @-
```

4. Push to remote

```bash
❯ jj git push --bookmark main
```

## Example

Below is a full example on this repository. 

I implemented a feature use Claude Code Web which created a remote git branch. After fetching the remote branch with `jj` and testing the fix, I wanted to rebase it on main.

```bash
❯ jj ll --no-pager -n 5
@  kpxkvxnu (empty) (no description set) 7 minutes ago
◆  rwwxqqkl feat(til): On Reusing Agents And Commands Between Opencde And Claude Code main git_head() 15 minutes ago
◆  swuytkow fix(til): Shorter procedure to remove a file from tracking 19 hours ago
│ ◆  kwryxrts refactor(build): move _index.md generation to build step claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms@origin 1 day ago
├─╯
◆  oxyszprn feat(til): CHOP Instead Of Vibe Coding 2 days ago

❯ jj rebase -r kw -d main
Error: Commit 17c2465a1b3d is immutable
Hint: Could not modify commit: kwryxrts 17c2465a claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms@origin | refactor(build): move _index.md generation to build step
Hint: Immutable commits are used to protect shared history.
Hint: For more information, see:
      - https://jj-vcs.github.io/jj/latest/config/#set-of-immutable-commits
      - `jj help -k config`, "Set of immutable commits"
Hint: This operation would rewrite 1 immutable commits.

❯ jj bookmark track claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms@origin
Started tracking 1 remote bookmarks.
❯ jj ll --no-pager -n 5
@  kpxkvxnu (empty) (no description set) 9 minutes ago
◆  rwwxqqkl feat(til): On Reusing Agents And Commands Between Opencde And Claude Code main git_head() 16 minutes ago
◆  swuytkow fix(til): Shorter procedure to remove a file from tracking 19 hours ago
│ ○  kwryxrts refactor(build): move _index.md generation to build step claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms 1 day ago
├─╯
◆  oxyszprn feat(til): CHOP Instead Of Vibe Coding 2 days ago

❯ jj rebase -r kw -d main
Rebased 1 commits onto destination

❯ jj ll --no-pager -n 5
@  kpxkvxnu (empty) (no description set) 9 minutes ago
│ ○  kwryxrts refactor(build): move _index.md generation to build step claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms* 3 seconds ago
├─╯
◆  rwwxqqkl feat(til): On Reusing Agents And Commands Between Opencde And Claude Code main git_head() 16 minutes ago
◆  swuytkow fix(til): Shorter procedure to remove a file from tracking 19 hours ago
◆  oxyszprn feat(til): CHOP Instead Of Vibe Coding 2 days ago

❯ jj edit kw
Working copy  (@) now at: kwryxrts db70e678 claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms* | refactor(build): move _index.md generation to build step
Parent commit (@-)      : rwwxqqkl 5f061e68 main | feat(til): On Reusing Agents And Commands Between Opencde And Claude Code
Added 0 files, modified 1 files, removed 3 files

❯ jj ll --no-pager -n 5
@  kwryxrts refactor(build): move _index.md generation to build step claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms* 21 seconds ago
◆  rwwxqqkl feat(til): On Reusing Agents And Commands Between Opencde And Claude Code main git_head() 17 minutes ago
◆  swuytkow fix(til): Shorter procedure to remove a file from tracking 19 hours ago
◆  oxyszprn feat(til): CHOP Instead Of Vibe Coding 2 days ago
◆  qumyqpmt feat(til): Zed: Add colourize brackets 4 days ago

❯ jj new
Working copy  (@) now at: yyxzpoqr a118d9ce (empty) (no description set)
Parent commit (@-)      : kwryxrts db70e678 claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms* | refactor(build): move _index.md generation to build step

❯ jj ll --no-pager -n 5
@  yyxzpoqr (empty) (no description set) 2 seconds ago
○  kwryxrts refactor(build): move _index.md generation to build step claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms* git_head() 35 seconds ago
◆  rwwxqqkl feat(til): On Reusing Agents And Commands Between Opencde And Claude Code main 17 minutes ago
◆  swuytkow fix(til): Shorter procedure to remove a file from tracking 19 hours ago
◆  oxyszprn feat(til): CHOP Instead Of Vibe Coding 2 days ago
❯ jj bookmark set main -r @-
Moved 1 bookmarks to kwryxrts db70e678 claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms* main* | refactor(build): move _index.md generation to build step

❯ jj ll --no-pager -n 5
@  yyxzpoqr (empty) (no description set) 36 seconds ago
○  kwryxrts refactor(build): move _index.md generation to build step claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms* main* git_head() 1 minute ago
◆  rwwxqqkl feat(til): On Reusing Agents And Commands Between Opencde And Claude Code main@origin 17 minutes ago
◆  swuytkow fix(til): Shorter procedure to remove a file from tracking 19 hours ago
◆  oxyszprn feat(til): CHOP Instead Of Vibe Coding 2 days ago

❯ jj git push --bookmark main
Changes to push to origin:
  Move forward bookmark main from 5f061e6882a7 to db70e678380d
remote: Resolving deltas: 100% (5/5), completed with 5 local objects.

❯ jj ll --no-pager -n 5
@  yyxzpoqr (empty) (no description set) 1 minute ago
◆  kwryxrts refactor(build): move _index.md generation to build step claude/move-index-generation-019HJ19hL29wt2QJbmgcBVms* main git_head() 1 minute ago
◆  rwwxqqkl feat(til): On Reusing Agents And Commands Between Opencde And Claude Code 18 minutes ago
◆  swuytkow fix(til): Shorter procedure to remove a file from tracking 19 hours ago
◆  oxyszprn feat(til): CHOP Instead Of Vibe Coding 2 days ago
```

_Created: 2025-12-08_
