# Opencode Filtering Models

When you have providers configured in Opencode that offer a lot of models, the model list can become lengthy even when favouriting models. 

You can filter models by a combination of the `enabled_providers` field and `whitelist` on the `provider`s. 

Here is an example from my current `.config/opencode/opencode.json`:

```json
{
  "enabled_providers": ["opencode", "mistral", "openrouter"],
  "provider": {
    "opencode": {
      "whitelist": [
        "gpt-5.2",
        "gpt-5.2-codex",
        "kimi-k2-thinking",
        "gemini-3-flash",
        "claude-opus-4-5",
        "claude-sonnet-4-5",
        "claude-haiku-4-5",
        "glm-4.7-free",
        "minimax-m2.1-free"
      ]
    },
    "mistral": {
      "whitelist": [
        "devstral-2512",
        "labs-devstral-small-2512"
      ]
    },
    "openrouter": {
      "whitelist": [
        "mistralai/mistral-nemo:free"
      ]
    }
  }
}
```

_Created: 2026-01-20_
