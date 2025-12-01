{
  description = "TIL - Today I Learned site (Zola)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            just
            python3
            zola
          ];

          shellHook = ''
            echo "TIL dev shell"
            echo "Zola version: $(zola --version)"
            echo ""
            echo "Available commands:"
            echo "$(just --list)"
            echo ""
          '';
        };
      });
}
