# Opencode: Use Codex through your OpenAI ChatGPT Plan

By default Opencode does not support Codex using your OpenAI ChatGPT Plus/Pro plan but with [this Opencode plugin](https://github.com/numman-ali/opencode-openai-codex-auth) you can. 

Opencode supports Anthropic/Claude Code plan out of the box and you can use a ChatGPT subscription in the same way. I like the setup of both plans with their daily and weekly limits and to be able to use both is pretty handy from the same CLI agent. 

Note the usage of the plugin comes with some caveats (see URL).

Steps:
1. Install the plugin 
2. Authenticate to your ChatGPT plan
3. Use the models you configured

## Install the plugin

Add to `~/.config/opencode/opencode.json`:

### The plugin declaration

```bash
{
  ...
  "plugin": [
    "opencode-openai-codex-auth@4.0.2"
  ],
  ...
```

### Model configuration

Add the Codex models you want to use through your ChatGPT Plus/Pro subscription. I seeded mine with the 13 variants Claude Sonnet suggested so I can prune or fine-tune them later, so the reasoning effort and output settings are explicit for granular control.

Note: This will need updating when new models come out.

```json
"provider": {
  "openai": {
    "options": {
      "reasoningEffort": "medium",
      "reasoningSummary": "auto",
      "textVerbosity": "medium",
      "include": [
        "reasoning.encrypted_content"
      ],
      "store": false
    },
    "models": {
      "gpt-5.1-codex-low": {
        "name": "GPT 5.1 Codex Low (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "low",
          "reasoningSummary": "auto",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-codex-medium": {
        "name": "GPT 5.1 Codex Medium (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "medium",
          "reasoningSummary": "auto",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-codex-high": {
        "name": "GPT 5.1 Codex High (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "high",
          "reasoningSummary": "detailed",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-codex-max": {
        "name": "GPT 5.1 Codex Max (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "high",
          "reasoningSummary": "detailed",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-codex-max-low": {
        "name": "GPT 5.1 Codex Max Low (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "low",
          "reasoningSummary": "detailed",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-codex-max-medium": {
        "name": "GPT 5.1 Codex Max Medium (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "medium",
          "reasoningSummary": "detailed",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-codex-max-high": {
        "name": "GPT 5.1 Codex Max High (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "high",
          "reasoningSummary": "detailed",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-codex-max-xhigh": {
        "name": "GPT 5.1 Codex Max Extra High (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "xhigh",
          "reasoningSummary": "detailed",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-codex-mini-medium": {
        "name": "GPT 5.1 Codex Mini Medium (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "medium",
          "reasoningSummary": "auto",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-codex-mini-high": {
        "name": "GPT 5.1 Codex Mini High (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "high",
          "reasoningSummary": "detailed",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-low": {
        "name": "GPT 5.1 Low (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "low",
          "reasoningSummary": "auto",
          "textVerbosity": "low",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-medium": {
        "name": "GPT 5.1 Medium (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "medium",
          "reasoningSummary": "auto",
          "textVerbosity": "medium",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      },
      "gpt-5.1-high": {
        "name": "GPT 5.1 High (OAuth)",
        "limit": {
          "context": 272000,
          "output": 128000
        },
        "options": {
          "reasoningEffort": "high",
          "reasoningSummary": "detailed",
          "textVerbosity": "high",
          "include": [
            "reasoning.encrypted_content"
          ],
          "store": false
        }
      }
    }
  }
}
```

This will get you:

**GPT-5.1 Codex family:**
- `gpt-5.1-codex-low` (low reasoning, auto summary)
- `gpt-5.1-codex-medium` (medium reasoning, auto summary)
- `gpt-5.1-codex-high` (high reasoning, detailed summary)

**GPT-5.1 Codex Max family:**
- `gpt-5.1-codex-max` (high reasoning, detailed summary)
- `gpt-5.1-codex-max-low` (low reasoning, detailed summary)
- `gpt-5.1-codex-max-medium` (medium reasoning, detailed summary)
- `gpt-5.1-codex-max-high` (high reasoning, detailed summary)
- `gpt-5.1-codex-max-xhigh` (xhigh reasoning, detailed summary) ✓

**GPT-5.1 Codex Mini family:**
- `gpt-5.1-codex-mini-medium` (medium reasoning, auto summary)
- `gpt-5.1-codex-mini-high` (high reasoning, detailed summary)

**GPT-5.1 base family:**
- `gpt-5.1-low` (low reasoning, low verbosity)
- `gpt-5.1-medium` (medium reasoning, medium verbosity)
- `gpt-5.1-high` (high reasoning, high verbosity)

### Install the plugin

Starting Opencode will install the plugin.

```bash
# Restart OpenCode (auto-installs plugin)
opencode
```

## Authenticate with ChatGPT Plus/Pro

```bash
# Authenticate
# Select: OpenAI → ChatGPT Plus/Pro (Codex Subscription)
opencode auth login

# Test
opencode run "who are you?" --model=openai/gpt-5.1-codex-medium
```

## Select and use

```bash
# Explore models, in `opencode`:
/models
```

Will give you:

![ChatGPT plan in Opencode](images/chatgpt-plan-in-opencode.png)


_Created: 2025-12-09_
