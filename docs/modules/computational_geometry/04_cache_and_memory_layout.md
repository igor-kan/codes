# Cache Locality & Memory Layout: Convex Hull & Delaunay Triangulation

## 1. Memory Layout Architecture

To maximize L1 data cache throughput (64 bytes/cacheline), data structures in `computational_geometry` are arranged using **Struct of Arrays (SoA)** rather than Array of Structs (AoS) whenever SIMD processing is active.

```
AoS (Sub-optimal for SIMD):
[ (x0, y0, z0, w0) | (x1, y1, z1, w1) | (x2, y2, z2, w2) ... ]

SoA (Optimal for SIMD & Pre-fetching):
[ x0, x1, x2, x3, ... | y0, y1, y2, y3, ... | z0, z1, z2, z3, ... ]
```

## 2. Cache Miss Penalty Mitigation

1. **Sequential Strides**: Inner loops iterate strictly with stride-1 access patterns, ensuring hardware prefetchers stream contiguous cachelines without stalls.
2. **Cache Tiling / Blocking**: Large multidimensional domains are partitioned into tiles of size $B \times B$ where:

$$2 \cdot B^2 \times \text{sizeof}(float64) \le \text{L1 Cache Size} (32 \text{ KiB})$$

Yielding optimal tile dimension $B = 32$ or $B = 48$.
