{
  description = "Advent of Code in Rust";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
    rust-overlay.url = "github:oxalica/rust-overlay";
  };

  outputs = { self, nixpkgs, flake-utils, rust-overlay }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        overlays = [ rust-overlay.overlays.default ];
        pkgs = import nixpkgs { inherit system overlays; };
        clangVersion = pkgs.lib.versions.major pkgs.llvmPackages.libclang.version;
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pkgs.rust-bin.stable.latest.complete
            pkgs.cargo-watch
            pkgs.llvmPackages.libclang
            pkgs.llvmPackages.clang
            pkgs.z3.dev
            # Sometimes helpful to explicitly include glibc headers if stdio.h fails later
            pkgs.glibc.dev
          ];
          shellHook = ''
            export LIBCLANG_PATH="${pkgs.llvmPackages.libclang.lib}/lib"
            export BINDGEN_EXTRA_CLANG_ARGS="
              -I ${pkgs.z3.dev}/include
              -isystem ${pkgs.llvmPackages.libclang.lib}/lib/clang/${clangVersion}/include
              -isystem ${pkgs.glibc.dev}/include
            "
          '';
        };
      }
    );
}

