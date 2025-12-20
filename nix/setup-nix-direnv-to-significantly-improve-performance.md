# Setup nix-direnv To Significantly Improve Performance

Enabling [nix-direnv](https://github.com/nix-community/nix-direnv?tab=readme-ov-file#nix-direnv) significantly improves performance by caching flake environments:

In .config/home-manager/home.nix:

```bash
programs.direnv = {
 enable = true;
 nix-direnv.enable = true;
};
```

This caches dev shells and prevents Nix from garbage collecting them, making direnv much faster.

_Created: 2025-12-20_
