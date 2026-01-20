# Declarative Package Management With Homebrew

Homebrew provides declarative package management through the `brew bundle` command with the `--cleanup` flag.

If a `Brewfile` contains packages:

```text
cask "firefox"
cask "ghostty"
cask "proton-mail"
cask "zed"
cargo "cargo-audit"
cargo "cargo-nextest"
cargo "cargo-watch"
```

When:

```bash
brew bundle install --cleanup --file=Brewfile
```

Then all packages declared in the file will be installed. The `--cleanup` flag ensures that packages removed from the Brewfile are also uninstalled from your system.



_Created: 2026-01-20_
