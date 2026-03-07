# Fix `Did you mean devShell?` by exporting `devShells.default`

CI failed with:

```text
error: flake '...' does not provide attribute 'devShells.x86_64-linux.default' or 'packages.x86_64-linux.default'
       Did you mean devShell?
```

`devShells.<system>.default` is expected here. `flake.nix` was exporting `devShell`, which [is a legacy flake output key since Nix 2.7](https://nix.dev/manual/nix/2.24/release-notes/rl-2.7).

So change:

```nix
devShell = pkgs.mkShell {
```

Into:

```nix
devShells.default = pkgs.mkShell {
```

Inside a per-system output block, `devShells.default` means the default development shell for that system (which becomes `devShells.<system>.default` at the top-level flake output).

Why this started failing now (likely): in my CI (early 2026), Determinate Nix behavior exposed the legacy key usage, so applying the [Nix 2.7](https://nix.dev/manual/nix/2.24/release-notes/rl-2.7) rename fixed it.

_Created: 2026-03-06_
