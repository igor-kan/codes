# Compiler Optimizations & Toolchain Flags: Convex Hull & Delaunay Triangulation

## 1. Recommended Production Build Flags

To unlock peak performance in `computational_geometry`, the following compiler flags are recommended:

```bash
# Production GCC / Clang Flags:
-O3 -march=native -mtune=native -flto -fno-math-errno -fno-trapping-math
```

## 2. Flag Breakdown

- `-O3`: Enables aggressive auto-vectorization, loop interchange, and inline optimizations.
- `-march=native`: Emits instructions specifically tailored to the host CPU's instruction set (AVX2, AVX-512, FMA).
- `-flto`: Link-Time Optimization performs cross-translation-unit inlining and dead-code elimination across module boundaries.
