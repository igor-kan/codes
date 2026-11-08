# Dijkstra Shortest Path with Fibonacci Priority Queue (`dijkstra_fibonacci`)

## Architectural Specification

The `dijkstra_fibonacci` module provides advanced algorithmic capabilities for `codes`.

### Component Artifacts

- **Types & Configuration**: [`types.md`](./types.md)
- **Abstract Interface**: [`interface.md`](./interface.md)
- **Core Computational Kernel**: [`core.md`](./core.md)
- **Unit Verification**: [`test_unit.md`](./test_unit.md)
- **Boundary Guards**: [`boundary.md`](./boundary.md)
- **SIMD Accelerations**: [`perf_simd.md`](./perf_simd.md)
- **Cache Locality Tiling**: [`cache_locality.md`](./cache_locality.md)
- **Concurrency & Reentrancy**: [`concurrency.md`](./concurrency.md)
- **Microbenchmarking**: [`benchmarks.md`](./benchmarks.md)
- **Continuous Fuzzing Target**: [`fuzz_target.md`](./fuzz_target.md)
- **Crash Regression Suite**: [`regression.md`](./regression.md)
- **Formal Invariants**: [`invariants.md`](./invariants.md)
- **Error Diagnostics**: [`errors.md`](./errors.md)
- **Diagnostic Runner CLI**: [`cli.md`](./cli.md)

### Operational Complexity

| Operation | Time Complexity | Auxiliary Space |
| :--- | :--- | :--- |
| **Transform** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Tile Cache**| $\mathcal{O}(N \log N)$ | $\mathcal{O}(1)$ |

---
*Maintained under continuous integration and sanitizer testing.*
