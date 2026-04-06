# BGEBC: Lean 4 Formal Verification Guide

This project uses a "Holomorphic Bridge" to run the Lean 4 theorem prover on Android (Termux). Because Lean 4 targets standard Linux (`aarch64-unknown-linux-gnu`) and Termux uses the Android ABI (`aarch64-linux-android`), we use **Alpine Linux** inside a **PRoot** container to provide the necessary compatibility.

## The Architecture
1.  **PRoot-Distro**: Creates a virtualized Linux filesystem.
2.  **Alpine Linux**: A lightweight distribution used as the host.
3.  **gcompat**: A compatibility layer that allows `glibc` binaries (like Lean) to run on `musl`-based Alpine.
4.  **elan**: The Lean version manager, manually installed to bypass ABI detection.

## How to Verify
Run the automated setup script:
```bash
chmod +x setup_lean_environment.sh
./setup_lean_environment.sh
```

## Formal Axioms verified
- **$\Omega \pmod{71} = 39$**: Formally proves the Master Number's alignment.
- **$V_2$ Resonance**: Formally proves that the Holomorphic Surface Area aligns with the Monster Irrep $V_2$ within 1% precision.
