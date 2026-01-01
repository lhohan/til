# Opencode Prompt Locations


Built-in Prompt Locations:

- Base prompt loader/injection logic sits in SessionPrompt.insertReminders at https://github.com/sst/opencode/blob/dev/packages/opencode/src/session/prompt.ts#L1003 (look for the PROMPT_PLAN and BUILD_SWITCH pushes).  
- Plan-mode text itself lives in https://github.com/sst/opencode/blob/dev/packages/opencode/src/session/prompt/plan.txt. It’s appended to the base prompt whenever the plan agent is active.  
- Model-specific base prompts for Build mode are under packages/opencode/src/session/prompt/. Example Anthropic prompt: https://github.com/sst/opencode/blob/dev/packages/opencode/src/session/prompt/anthropic.txt (others in that folder cover codex, gemini, qwen, etc.).  
- Build ↔ Plan behavior is identical except for the injected plan.txt plus permissions. Permissions are defined in Agent at https://github.com/sst/opencode/blob/dev/packages/opencode/src/agent/agent.ts#L34-L122. The planPermission block at lines 47–76 denies edits and restricts bash; the plan agent simply reuses the base prompt while applying that permission set at lines 82–95.  
- Explore subagent prompt (file search specialist) resides at https://github.com/sst/opencode/blob/dev/packages/opencode/src/agent/prompt/explore.txt.  
- Utility prompts for compaction/title/summary live alongside it, e.g. compaction: https://github.com/sst/opencode/blob/dev/packages/opencode/src/agent/prompt/compaction.txt.

In short: Build mode uses whichever base prompt matches its model; Plan mode takes that same prompt, appends plan.txt via insertReminders, and enforces the stricter permissions block from agent.ts.

_Created: 2025-12-18_
