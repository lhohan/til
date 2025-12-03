# Claude Code Mcp Management

When my Context7 MCP stopped working in Claude Code (due to SSE event support being deprecated) I started looking into how MCP servers are actually managed. My main interest: how do I manage my MCP setup so it is easy to switch machines?

Claude manages a `~/.claude.json` file for internal state like MCP servers (but also other concerns, here I'll only consider MCPs), and keeps track how they are managed locally: at project level or user level. User level meaning, if an MCP is managed at this level, it is available to all projects on your machine. These MCPs are managed by using the `claude mcp add` and `claude mcp remove` command.

Claude also provides settings files in which you can manage MCP servers through: `settings.json`, `settings.local.json` and `.mcp.json` files at project level (in `.claude/...`) or user level (in `~/claude/...`). These MCPs are managed by editing the JSON files directly. (To be precise, `.mcp.json` can also be manage with `claude mcp` command.)

**It is important to keep in mind how you manage MCPs because of credentials.** That is why it makes sense for Claude to manage its global config in the home directory and not at the project level. It is also why I think it is better to manage your MCP through the `claude mcp` commands. In other words: avoid managing MCPs in the settings files, except for when you need: 
- project and team level MCPs, which I manage in `.mcp.json`
- version control, probably only applies for team and private configs
- complex setup with variable expansion (I have no use case for this, found it in Claude docs, thought it may be worthwhile mentioning)

From usage perspective I do not think there is much difference between managing MCPs with `claude mcp` commands (config stored in `~/.claude.json`) or manually edditing `.mcp.json`. If you want to version control them personally, you can use a `dotfiles` setup (providing you do no not need MCP servers installed?).

The main downside of `claude mcp add` is that it doesn't allow easy editing after creation (`claude mcp remove` and try again) but I'm ok with that. 

Overview to decide which `claude mcp add` command to use:

| Scope   | CLI Flag                | Where It's Stored                                  | Use Case                                        |
|---------|-------------------------|----------------------------------------------------|-------------------------------------------------|
| Local   | --scope local (default) | Project-specific user settings (managed by Claude) | Personal configs for current project |
| Project | --scope project         | .mcp.json at project root (VCS-tracked)            | Team level - e.g. shared servers                             |
| User    | --scope user            | User-wide settings (managed by Claude)             | Personal config all projects          |

'managed by Claude' means: stored in `~/.claude.json`.

Given all this, to move between machines I would expand my `dotfiles` setup but I am not sure that at this point it is worthwhile already. I will _not_ be adding the `~/.claude.json` file for sure as it contains reference to projects I may not have checked out (yet or ever) on a new machine. _Maybe_ `~/.claude/.mcp.json` could be version controlled but, if I would go this route, **I would resort to managing a simple `claude-code.sh` containing `claude mcp add ...` commands**.

_Created: 2025-12-03_
