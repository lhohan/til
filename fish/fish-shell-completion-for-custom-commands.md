# Fish Shell Completion For Custom Commands

Any custom CLI tool can get tab completion if the tool supports getting its CLI arguments from itself. 

Example: a small profile wrapper (`agentic <profile>`) that reads its profiles from `~/.config/agentic/profiles.yaml`. (I created it to start agents with specific models, settings or system prompts.)

```fish
# ~/.config/fish/completions/agentic.fish
complete -c agentic -f -a "(agentic --list-profiles)"
```

- `complete -c <command>` registers a completion rule for that command.
- `-f` disables file completion, so TAB never falls back to completing filenames.
- `-a "(...)"` is a command substitution: fish runs it on every TAB press and uses the output lines as candidates.

Three things make the rest automatic:

1. **Fish autoloads completions.** Any file at `~/.config/fish/completions/<command>.fish` is sourced lazily the first time completion for `<command>` is requested.

2. **The TAB-as-description convention.** When a candidate contains a TAB character, fish renders the part before the tab as the completion and the part after it as the grey description on the right. So the wrapper prints `name<TAB>description` (`printf '%s\t%s\n'`) and the shell never parses the config itself  (the separator has to be a real tab byte).

3. **Single source of truth.** The completion knows nothing about the config format, it asks the tool. Every TAB re-runs the command, so a profile added to the config appears immediately with its description; no shell restart, no re-registration. Profiles without a description yield the bare name.

Verify without pressing TAB:

```fish
$ fish -c 'complete -C"agentic "'
fast	Pi with a fast model
private Vibe with mistral and local models
```

_Created: 2026-09-29_
