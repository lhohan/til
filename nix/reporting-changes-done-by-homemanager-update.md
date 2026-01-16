# Reporting Home Manager Package Changes During Updates

Use `nvd` with Home Manager's activation hook to report package changes during updates.

Example output:

```
<<< .../.local/state/nix/profiles/home-manager-65-link
>>> .../.local/state/nix/profiles/home-manager-66-link
Version changes:
[U.]  #1  claude-code  2.1.7 -> 2.1.9
[U.]  #2  codex        0.84.0 -> 0.86.0
[U.]  #3  opencode     1.1.20 -> 1.1.23
Closure size: 408 -> 408 (9 paths added, 9 paths removed, delta +0, disk usage +1,011.2KiB).
```

Add this `home.activation` block to your `home.nix` configuration:

```nix
{ config, pkgs, ... }:

{
  # ... existing configuration ...

  home.activation.report-changes = config.lib.dag.entryAnywhere ''
    if [[ -n "$oldGenPath" && "$oldGenPath" != "$newGenPath" ]]; then
      ${pkgs.nvd}/bin/nvd diff "$oldGenPath" "$newGenPath"
    fi
  '';
}
```

**Key Points:**
- `nvd` ([Nix/NixOS package version diff tool](https://khumba.net/projects/nvd/)) provides human-readable package summaries.
- The `$oldGenPath` and `$newGenPath` variables are provided automatically by Home Manager during activation.
- Using `${pkgs.nvd}` ensures the tool is available without adding it to your global environment.
- The `if` statement guards against the first activation and no-change scenarios.

_Created: 2026-01-16_
