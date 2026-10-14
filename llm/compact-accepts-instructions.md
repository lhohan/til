# `/compact` Accepts Instructions

Many coding agents provide a `/compact` command to summarise the conversation and free context space. The command can also accept instructions about what to preserve:

```text
/compact Only keep the plan location and outcome we decided on.
```

Without instructions, the agent chooses what to emphasise in the summary. An explicit instruction is useful after a conversation has gone off track, such as when it contains side discussions or several abandoned approaches. It directs the compacted context back towards the active task instead of leaving the emphasis implicit.


_Created: 2026-10-14_
