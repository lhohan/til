# Claude Code Web On A New Repo Sets Default Branch Not To Main

When I start projects using [Claude Code web](http://claude.ai/web) on new, empty GitHub repositories, I've noticed Claude sets the default branch to the branch it creates itself.

If you haven't set a `Default branch` (such as `main`) yet, Claude will set it to the branch it creates for the feature you've asked it to implement. This means all subsequent Claude Code sessions will start from that initial branch unless you change the default.

To avoid this, you have two options:

- **Before starting with Claude**: Create a `main` branch when you create the repository and set it as the default. This ensures Claude's work branches off from `main`.
- **After starting with Claude**: Create a `main` branch manually and set it as the default branch in your repository settings. Then, if needed, rebase or merge Claude's work onto `main`.

_Created: 2025-12-15_
