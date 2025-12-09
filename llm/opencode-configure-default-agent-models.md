# Opencode: Configure Default Agents' Model

Out of the box open code supports two modes `plan` and `build`. Here is how you can make the configuration of these plans explicit and also define the models to be used for each.

In `~/.config/opencode/opencode.json`:

```json
{
  ...
  "agent": {
      "build": {
        "model": "anthropic/claude-haiku-4-5",
        "temperature": 0.3,
        "tools": {
          "write": true,
          "edit": true,
          "bash": true
        }
      },
      "plan": {
        "model": "anthropic/claude-sonnet-4-5",
        "temperature": 0.1,
        "tools": {
          "write": false,
          "edit": false,
          "bash": true,
          "exa": true
        }
      }
    }
```

_Created: 2025-12-09_
