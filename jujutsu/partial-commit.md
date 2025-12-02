# Partial commit

TLDR: Use `jj commit -m "..." <files>`, not `jj split`, to commit related changes from a working copy that contains unrelated changes.


When having changes in your working copy that belong to a different task, you can commit related changes with the standard `commit` command. You do **not** need to use the `split` command.
  
I was trying to use the `jj split` command to commit a subset of files without the diff editor appearing, but running `jj split` __always__ launches the diff editor. This is not what I wanted I just want to commit related changes to together without an editor popping up. 

After looking into it, it makes sense _why_ : `jj split` splits the actual commit. So you need to specify which files go into which commit. I was thinking of `jj split` as splitting 'the set of files currently in my working copy across commits', without giving much thought to what I meant by 'commits'.

Looking into the commit command: turns out, logical in retrospect, `jj commit` allows for files to be specified.

Key insights:
-  `jj split` splits a revision in two, `jj commit` creates a new commit.
-  `jj commit` accepts file paths

Given these findings it became clear I need to use `jj commit` when I want a new commit to contain only certain files from the working copy and don’t want an editor.

```bash
jj commit -m … <paths>
```

as example, an actual commit I did:

```bash
jj commit -m "style: Reduce homepage spacing and container width to 900px" static/css/main.css
```

- `-m` supplies the message, so no editor opens.
- List every path you want included; the rest of your working copy stays uncommitted.
- This creates a new commit on top of `@` with just that file’s changes.

Next to verify to ensure only the desired file landed in the new commit:
- `jj st --no-pager` : shows the changes left after the commit
- `jj show @-` or `jj diff -r @-..@` : shows the changes between the current ref and the previous one, in other words the changes done by the commit

If you truly need to split an existing commit in place (instead of making a new one) use `jj split`.
)

_Created: 2025-12-01_
