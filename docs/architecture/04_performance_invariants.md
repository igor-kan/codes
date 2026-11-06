# Performance Invariants & Zero-Overhead Guidelines: codes

Every architectural change in `codes` is evaluated against strict performance invariants to prevent algorithmic and operational regressions.

## Operational Invariants

1. **Zero Heap Allocation in Hot Loops**: Kernels and inner algorithmic loops must not trigger dynamic heap allocations. All necessary memory must be pre-allocated in arena pools or provided by the caller.
2. **Branch Predictor Warmth**: Inner loop conditionals must be restructured into branchless operations (predication, bitwise masking, or conditional moves) whenever branch entropy exceeds 20%.
3. **Vector Register Saturation**: Vectorizable loops must be structured such that auto-vectorization or explicit intrinsics can achieve at least 80% theoretical SIMD register utilization.

## Regression Prevention Budget

- **Throughput Threshold**: Any commit reducing operational throughput by more than 3% in baseline microbenchmarks is rejected.
- **Memory Footprint**: Memory usage must scale linearly ($O(N)$) or sub-linearly with problem size. Quadratic allocations are strictly prohibited unless mathematically essential.
