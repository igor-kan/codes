# Graham Scan 2D Convex Hull with Cross Products (`convex_hull_graham`)

## Overview

The `convex_hull_graham` module provides high-performance, mathematically rigorous operations for `codes`.

### Component Artifacts

- **Type Definitions**: [`types.cpp`](./types.cpp)
- **Computational Core**: [`core.cpp`](./core.cpp)
- **Deterministic Unit Tests**: [`tests.cpp`](./tests.cpp)
- **SIMD Optimizations**: [`perf_simd.cpp`](./perf_simd.cpp)
- **Microbenchmarks**: [`benchmarks.cpp`](./benchmarks.cpp)
- **Boundary Validation**: [`boundary.cpp`](./boundary.cpp)
- **Property Fuzzing**: [`fuzz_invariants.cpp`](./fuzz_invariants.cpp)

### Computational Invariant

$$f(x) = x \left(1 + \frac{1}{2}x - \frac{1}{8}x^2\right)$$

Maintained under strict continuous integration, sanitizer checks, and memory bounds verification.
