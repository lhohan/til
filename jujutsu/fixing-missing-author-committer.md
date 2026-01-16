# Fixing Missing Author or Committer on a Commit

Commits without author or committer information cannot be pushed to remote. To fix:

```bash
jj describe -r "$rev" --reset-author --no-edit
```

- Replace `$rev` with your change ID.
- `jj describe --reset-author` rewrites the commit using the current config's user.name/user.email for both author and committer fields.
- The `--no-edit` flag keeps the existing commit message.

For multiple commits:

```bash
for rev in nn to kn yx us qn wwz sq qx ytz zlq; do
  jj describe -r "$rev" --reset-author --no-edit
done
```

Replace the example change IDs with your own.

_Created: 2026-01-16_
