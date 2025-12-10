# Fix Broken Shift Enter In Ghostty when using Claude Code 

When using Claude Code in the Ghostty terminal `Shift-Enter` (on MacOS) outputs strange character sequences instead of going to the next line. `Shift-Enter` works in most other terminal interfaces and muscle memory is hard to change so this was quite annoying.

The issue: Ghostty terminal, doesn't insert a newline character for `Shift+Enter` by default.

A nice feature of Ghostty is that it is configurable through its `config` file: `~/.config/ghostty/config`. To fix the above issue all that is needed is to add a keybinding configuration:

```ini
# Fix Shift+Enter issue - make it insert a newline for multi-line input
# This allows Shift+Enter to work properly in applications like Claude Code
keybind = shift+enter=text:\x0a
```

`\x0a` is the hexadecimal representation of ther line feed (LF) character.

_Created: 2025-12-10_
