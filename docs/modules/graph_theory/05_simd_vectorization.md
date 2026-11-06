# SIMD Vectorization & Instruction Throughput: Strongly Connected Components & Matching

## 1. Vector Lane Utilization

The arithmetic kernel in `graph_theory` leverages data-parallel vector lanes across modern CPU architectures:

| Instruction Set | Vector Width | Float64 Lanes | Float32 Lanes | Register File |
| :--- | :--- | :--- | :--- | :--- |
| **AVX2 / FMA3** | 256 bits | 4 lanes | 8 lanes | YMM0 - YMM15 |
| **AVX-512** | 512 bits | 8 lanes | 16 lanes | ZMM0 - ZMM31 |
| **ARM Neon** | 128 bits | 2 lanes | 4 lanes | V0 - V31 |

## 2. Fused Multiply-Add (FMA) Optimization

Loops evaluate polynomial and dot-product expressions using FMA intrinsics ($a \cdot b + c$), halving instruction count and eliminating intermediate rounding steps:

```
// FMA vector accumulation pattern:
acc = _mm256_fmadd_pd(v_a, v_b, acc);
```

Loop unrolling factor is selected as $U = 4$ to hide the 4-cycle FMA pipeline latency and saturate execution ports.
