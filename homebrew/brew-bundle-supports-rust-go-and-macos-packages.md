# Brew Bundle Supports Rust, Go, and macOS Packages

You can [declare your brew packages using a Brewfile](declarative-package-management-with-homebrew).Beyond taps and casks, Brewfile also supports managing Rust packages, Go packages, and macOS App Store applications.

```text
# Taps (repositories)
tap "homebrew/cask-fonts"

# Core formulae (CLI tools)
brew "bat"

# GUI apps (casks)
cask "zed"

# Fonts
cask "font-jetbrains-mono-nerd-font"

# macOS apps from App Store (requires `mas` CLI)
mas "1Password", id: 443987910

# Rust
cargo "cargo-audit"

# Go
go "github.com/charmbracelet/crush"
```

See the [Brew bundle documentation](https://docs.brew.sh/Brew-Bundle-and-Brewfile) for more information.

_Created: 2026-01-20_
