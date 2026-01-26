# Opencode Disable Claude Code Compatibility

To disable Claude Code compatibility in Opencode, you can use any of these environment variables:

```bash
export OPENCODE_DISABLE_CLAUDE_CODE=1        # Disable all .claude support
export OPENCODE_DISABLE_CLAUDE_CODE_PROMPT=1 # Disable only ~/.claude/CLAUDE.md
export OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1 # Disable only .claude/skills
```

I use a shortcut shell script, `oc.sh`, to open Opencode with my preferred environment variables:

```bash
#!/usr/bin/env bash
set -euo pipefail

OPENCODE_DISABLE_CLAUDE_CODE=1 \
opencode "$@"
```

_Created: 2026-01-26_
