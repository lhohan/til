# Analyse Open Changes, Create Commit Message And Put It In The Clipboard

Sometimes I exit the LLM agent but still have changes open that I want to commit. Or I get back to a project with open changes. Instead of starting the CLI agent again, you can ask it to do this directly from the command line. 

I almost always want to review and edit the commit message, so rather than asking it to commit directly, I ask it to create the message and put it in the clipboard.

I put the prompt in a file (referred to as `give-me-a-commit-msg.md` below). Easier for editing and reuse with other LLMs. 

```markdown
Analyse the open changes with 'jj', focus on WHAT the change is about.
Create a concise commit message for these changes and put it in the clipboard.

Execute this bash command: `printf '%s' 'YOUR_COMMIT_MESSAGE' | pbcopy` (Replace YOUR_COMMIT_MESSAGE with the actual message, properly escaped.

Confirm you put the commit message in the clipboard.
```

Notes: 
- `jj`: I use Jujutsu day-to-day, so that is why this is in.
- These are simple instructions, if you want conventional commits you can add it there or refer to another file. Or analyse the last commits to follow existing project standards.
- I specify the exact `bash` command because Claude Code requires some permissions to be granted.

To run this prompt with Claude Code:

```bash
claude -p "$(< give-me-a-commit-msg.md)"  --permission-mode default --allowedTools "Bash(pbcopy:*),Bash(printf:*)" --model haiku
```

Claude needs extra arguments to copy to the clipboard. This took me some time to figure out, to be honest.

- `--permission-mode default` : I start Claude Code in _plan_ mode, so to run commands you need to change that. 
- `--allowedTools "Bash(pbcopy:*),Bash(printf:*)"`: Claude is strict with permissions so you need to grant execution of `pbcopy` and `printf`. This is why in the prompt I specify the exact command to copy to the clipboard, to make this part more deterministic.

Example output:

```bash
✓ **Commit message created and copied to clipboard:**

---
refactor: Move PATH configuration to home.sessionPath in Home Manager
---

**What changed:**
... CUT ...

The commit message is in your clipboard with no trailing newline.
```

And indeed in the clipboard (`Cmd-v`):
    
```bash
refactor: Move PATH configuration to home.sessionPath in Home Manager
```

Note: It's important to realize that each run will generate a different, hopefully similar, result given the nature of LLMs. As mentioned, *I use this as a starter for the actual commit and always verify*.

## Other agents

For the fun of it, I also tested this workflow with other CLI agents on my system.

### Mistral Vibe

At the time of writing only a few days released maybe this is why it does not require to approve any permissions. Since I am only reading the file system and putting content in the Clipboard, I am going to accept this risk. The model used is `Devstral 2` which seems to be very capable and maybe even overkill for this kind of tasks. Benefit: cheap compared to the other flagship models (currently free for limited time).

```bash
> vibe -p "$(< give-me-a-commit-msg.md)"
The commit message has been created and copied to the clipboard:

`chore: Fix Nix tests on macOS M4 and improve PATH management`
```


### Opencode

Opencode is more verbose. I'm unsure why this happens (Opencode setting, model configuration?) or if it's typical behaviour, but I don't mind. I have cut some parts out that are not relevant to focus on the more interesting parts.

Notable: it asks for permission to execute the command. At the time of writing I did not look in detail if I could pass flags to skip this.

Remark: because the prompt explicitly states the command to execute, we gain determinism but sacrifice some LLM creativity. Without this instruction, Opencode and the model it uses more often than not also _verified_ that the message was indeed copied to the clipboard, which I found pretty neat. (Sure, we can add that check to the prompt too if we wanted to.)

```bash
❯ opencode run "$(< give-me-a-commit-msg.md)"

I'll analyze the open changes using `jj` and create a commit message for you.

|  Bash     Check current working tree status

Working copy changes:
... CUT ...


|  Bash     Show all changes in the working directory

Modified regular file ../.config/home-manager/flake.nix:
... CUT ...
Modified regular file ../.config/home-manager/zsh.nix:
... CUT ...

Now I'll analyze the changes and create a commit message:

**Analysis of changes:**

1. ... CUT ...
2. ... CUT ...

**Commit message:**

---
Refactor PATH management via Home Manager and fix Nix build on macOS
---

Now I'll copy this to the clipboard:

│
◇  Permission required to run: printf "Refactor PATH management via Home Manager and fix Nix build on macOS" | pbcopy
│  Allow once
|  Bash     Copy commit message to clipboard

✓ **Commit message copied to clipboard:**

---
Refactor PATH management via Home Manager and fix Nix build on macOS
---

The message captures the two main changes:
... CUT ...
```

### Codex

I have also Codex on my system, but I haven't used it very often and I'm not familiar with the permission settings. I tried variations of `codex exec "$(< give-me-a-commit-msg.md)` with the `-a` flag but I kept running into permissions issues with `jj` and the clipboard commands. This was starting to take up more time than I wanted to invest in it so I stopped.

## Final script

I created a script I can run now in an dir, `give_me_a_commit_msg.sh`. It defaults to `vibe` at the moment because that's the least verbose and fastest at the moment.

```bash
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

vibe -p "$(< "$SCRIPT_DIR/give-me-a-commit-msg.md")"
# claude -p "$(< "$SCRIPT_DIR/give-me-a-commit-msg.md")"  --permission-mode default --allowedTools "Bash(pbcopy:*),Bash(printf:*)" --model haiku
# opencode run "$(< "$SCRIPT_DIR/give-me-a-commit-msg.md")"
```

_Created: 2025-12-11_
