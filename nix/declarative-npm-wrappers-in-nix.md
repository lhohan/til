# Declarative npm Wrappers in Nix

I wanted to install an npm CLI that isn't in nixpkgs or Homebrew ('Clavix'), but below approach works for other npm CLIs too.

In a Nix-managed environment, the global npm prefix is often read-only (/nix/store/...). Running `npm install -g clavix` fails because you cannot write to the Nix store imperatively.

The solution is to create a thin Nix-managed wrapper around a small shell script that uses `npx` to run the package on demand.

This example is a Home Manager snippet (for NixOS you can put the same wrapper into `environment.systemPackages`).

## Example: clavix.nix (link from `home.nix`)

```
{ pkgs, ... }:
{
  home.packages = [
    (pkgs.writeShellScriptBin "clavix" ''
      exec ${pkgs.nodejs}/bin/npx --quiet clavix@7.3.0 "$@"
    '')
  ];
}
```

Parameter breakdown:
*   `writeShellScriptBin "clavix"`: Creates a `clavix` executable on your `PATH`.
*   `exec`: Replaces the wrapper process with `npx`.
*   `${pkgs.nodejs}/bin/npx`: Uses the Nix-managed `nodejs`/`npx`, not whatever is on your `PATH`.
*   `--quiet`: Keeps output minimal.
*   `clavix@7.3.0`: Pins the npm package version.
*   `$@`: Forwards all args (e.g. `clavix --help`).

Benefit: it won't interfere with other Node projects or system-level permissions.

Trade-off: this is only "declarative" for the wrapper: `npx` fetches at runtime and caches under `~/.npm/_npx_` (so not fully offline/reproducible). Remove the wrapper and the command disappears from `PATH`, but the cache can stick around so manual cleanup is still needed.

_Created: 2026-02-24_
