let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in pkgs.mkShell {
  packages = [
    pkgs.python3
    pkgs.pnpm
    pkgs.nodejs_22
  ];

  # activate venv
  shellHook = ''
    source .venv/bin/activate
  '';
}
