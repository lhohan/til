# Install And Manage CLI Agents Using Nix Home Manager

Thus far, I've been installing, and hopefully uninstalling, my CLI agents using Homebrew. I recently found how I could manage them with [Home Manager using Nix](https://github.com/nix-community/home-manager). Below is how I set it up. 

Numtide provides Nix packages for LLM agents and updates them daily. Here is a list of all supported LLM agents: [llm-agents.nix](https://github.com/numtide/llm-agents.nix). I use different modules for different concerns. In this case, I use a module to keep all LLM agents in a dedicated `.nix` file.

## Add llm-agents.nix dependency to flake.nix

Flake inputs are top-level declarations. In Nix flakes, all inputs must be declared at the flake level in `flake.nix`. This is a fundamental constraint of the flake system. It would have been nicer, for modularity, to declare the dependency alongside the agents.
 
  - In `inputs` I declare the llm-agents dependency
  - In `outputs` I declare this dependency should be passed to all Home Manager modules
 
 ```nix
 {
 ...
   inputs = {
     nixpkgs.url = "github:nixos/nixpkgs/25.05";
     home-manager = {
       url = "github:nix-community/home-manager/release-25.05";
       inputs.nixpkgs.follows = "nixpkgs";
     };
     llm-agents.url = "github:numtide/llm-agents.nix";
   };
 
   outputs = { nixpkgs, home-manager, llm-agents, ... }:
     let
       ...
     in {
        ...
         # extraSpecialArgs to pass through arguments to all home-manager modules
         extraSpecialArgs = {
           inherit llm-agents;
         };
       };
     };
 }
```

## Add new module to `home.nix`

In `home.nix`, I declare my separate module files. So here I add the new `llm-agents.nix` file.

```nix
{ config, pkgs, ... }:

{
  ...
  # imports for modularity
  imports = [
    ./git.nix
    ./zsh.nix
    ./llm-agents.nix
  ];

  ... more config, install other packages, programs, etc ...
}
```

## Declare LLM agent packages in llm-agents.nix

Below is the complete file with the LLM agents I want on my system. At the time of writing, I mostly use `Claude Code` and `Opencode`. 

Note the `llm-agents` import at the top.

```nix
{ config, pkgs, lib, llm-agents, ... }:

{
  # LLM agent tools from https://github.com/numtide/llm-agents.nix
  home.packages =
    if llm-agents.packages ? ${pkgs.system}
    then with llm-agents.packages.${pkgs.system}; [
      ccusage
      claude-code
      crush
      codex
      mistral-vibe
      opencode
    ]
    else [];
}
```


_Created: 2025-12-16_
