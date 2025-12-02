# Untracking an already commited file

I accidentally commited a file that should not be tracked. If there is no sensitive data in it (yet), here is how you can remove it from the working copy.

I already have the file in `.gitignore`. And I changed it, this is often when I notice it should not have been committed in the first place, so it shows as modified in Jujutsu. Running `jj file untrack` deletes the local file instead of just stopping version control tracking. I still want to keep the file locally.

To untrack a file that's already in repository history while keeping your local copy:

```bash
# Using a Claude local settings file as an example.

# 1. Back up the file
cp .claude/settings.local.json .claude/settings.local.json.backup

# 2. Remove from tracking (remove from working copy)
rm .claude/settings.local.json

# 3. Commit the removal
jj commit -m "Remove .claude/settings.local.json from tracking"

# 4. Restore your local copy
mv .claude/settings.local.json.backup .claude/settings.local.json

# 5. Verify it's ignored
jj st --no-pager
```

Adding a file to `.gitignore` only prevents tracking **new** files. If a file was already tracked and committed in previous revisions, Jujutsu continues tracking it despite the `.gitignore` entry.

To stop tracking, you must explicitly remove it from the repository tree. Since it exists in the parent commit, removing it from tracking requires removing it from the working copy, requiring manual restoration of your local version.

There's no single command for "untrack but keep local" (understandably).

Note: I used `rm` directly instead of `jj file untrack` which would have the same effect. I prefer the direct `rm`-remove because it is more intentional: we are explicitly removing the file from the repository. `jj file untrack` is/feels more designed to stop tracking a file in the working copy that has not been committed yet.

_Created: 2025-12-02_
