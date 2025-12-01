+++
title = "[DEMO] Interactive rebase with autosquash"
date = 2024-11-15
[taxonomies]
topics = ["git"]
+++

When you have commits prefixed with `fixup!` or `squash!` followed by another commit's message, Git can automatically reorder and mark them during interactive rebase.

```bash
git rebase -i --autosquash main
```

To create a fixup commit that will be auto-squashed:

```bash
git commit --fixup=<commit-hash>
```

You can also enable this by default:

```bash
git config --global rebase.autosquash true
```

This is incredibly useful for cleaning up a feature branch before merging.
