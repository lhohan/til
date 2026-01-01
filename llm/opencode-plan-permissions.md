# Opencode Plan Permissions

In an earlier TIL I added explicit configuration of the `plan` agent to `opencode.json`. The permissions were missing but I [found them](https://github.com/sst/opencode/blob/49b4b5907e6a73870e967e6792d29f7a435942c2/packages/opencode/src/agent/agent.ts#L64-105) in the source code of Opencode. This is my updated `plan` config:

```json
"plan": {
      "model": "anthropic/claude-sonnet-4-5",
      "temperature": 0.1,
      "tools": {
        "write": false,
        "edit": false,
        "bash": true,
        "exa": true
      },
      "permission": {
        "edit": "deny",
        "bash": {
          "cut*": "allow",
          "diff*": "allow",
          "du*": "allow",
          "file *": "allow",
          "find * -delete*": "ask",
          "find * -exec*": "ask",
          "find * -fprint*": "ask",
          "find * -fls*": "ask",
          "find * -fprintf*": "ask",
          "find * -ok*": "ask",
          "find *": "allow",
          "git diff*": "allow",
          "git log*": "allow",
          "git show*": "allow",
          "git status*": "allow",
          "git branch": "allow",
          "git branch -v": "allow",
          "grep*": "allow",
          "head*": "allow",
          "less*": "allow",
          "ls*": "allow",
          "more*": "allow",
          "pwd*": "allow",
          "rg*": "allow",
          "sort --output=*": "ask",
          "sort -o *": "ask",
          "sort*": "allow",
          "stat*": "allow",
          "tail*": "allow",
          "tree -o *": "ask",
          "tree*": "allow",
          "uniq*": "allow",
          "wc*": "allow",
          "whereis*": "allow",
          "which*": "allow",
          "*": "ask"
        },
        "webfetch": "allow"
      }
    }
  },
```

To be honest, while I like them to be explicit I am not 100% sure yet if I will keep them. Now I mainly use them to get insight in the permission system while I use Opencode: when does Opencode ask me to ask for permission or not? And can I tweak these so I can Opencode run with less restrictions?

_Created: 2025-12-18_
