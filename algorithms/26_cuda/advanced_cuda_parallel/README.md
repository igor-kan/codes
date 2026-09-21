# Advanced CUDA Parallel Algorithms Suite

Parallel GPU computing kernels following the NVIDIA *CUDA C Programming Guide* and *CUDA C Best Practices*.
Includes `.cuh` headers, `.cu` implementation kernels, and host verification runners:
1. `parallel_reduction_warp` - Warp shuffle `__shfl_down_sync` block tree reduction
2. `prefix_sum_scan` - Blelloch work-efficient exclusive prefix sum scan
3. `matrix_transpose_shared_mem` - Conflict-free shared memory padded matrix transpose
4. `radix_sort_gpu` - Parallel least-significant-digit (LSD) radix sorting
5. `convolution_2d_constant_mem` - 2D spatial convolution utilizing cached `__constant__` memory
6. `monte_carlo_option_pricing` - Parallel Monte Carlo Black-Scholes pricing
7. `nbody_gravitational_tiling` - Tiled shared memory all-pairs gravitational acceleration
8. `histogram_atomic_privatized` - Per-block privatized shared memory histogram
9. `sparse_spmv_csr_vector` - Warp-per-row Compressed Sparse Row matrix-vector kernel
10. `heat_diffusion_2d_cuda` - 2D explicit stencil finite difference diffusion
