# Hardware Portability Matrix: Convex Hull & Delaunay Triangulation

## 1. Architectural Support Matrix

The `computational_geometry` implementation is designed for broad hardware portability across tier-1 platforms:

| Architecture | Vector Extension | Endianness | Status |
| :--- | :--- | :--- | :--- |
| **x86_64** | SSE4.2 / AVX2 / AVX-512 | Little-Endian | Tier 1 (Full SIMD) |
| **AArch64 (ARMv8/v9)** | Neon / SVE | Little-Endian | Tier 1 (Full SIMD) |
| **RISC-V (RV64GC)** | Standard / Vector Ext | Little-Endian | Tier 2 (Validated) |
| **GPU Accelerators** | CUDA / Metal / OpenCL | Little-Endian | Specialized Subsystems |

## 2. Fallback Implementations

On platforms lacking dedicated SIMD hardware, autovectorizer-friendly scalar loops provide correct reference results without platform-specific intrinsic requirements.
