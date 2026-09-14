# CUDA Kernels

Curated CUDA C++ source from [NVIDIA/cuda-samples](https://github.com/NVIDIA/cuda-samples)
(BSD-3-Clause), organized by the upstream sample categories. See `LICENSE` in this
directory for the original copyright. This module complements the portable
`03_cpp/` suite with GPU-specific programming models: thread/block indexing,
shared memory, warp intrinsics, streams, cooperative groups, tensor cores and
the CUDA libraries.

## Layout

| Directory | Upstream category | Focus |
|:---|:---|:---|
| `cpp/0_Introduction/` | Introduction | vectorAdd, asyncAPI, streams, textures, dynamic parallelism |
| `cpp/1_Utilities/` | Utilities | device query, topology, bandwidth test |
| `cpp/2_Concepts_and_Techniques/` | Concepts | reduction, scan, histogram, inlinePTX, eigenvalues |
| `cpp/3_CUDA_Features/` | CUDA features | cooperative groups, graph API, cluster launch |
| `cpp/4_CUDA_Libraries/` | CUDA libraries | cuBLAS, cuFFT, cuSPARSE, Thrust, CUB, NVJPEG |
| `cpp/5_Domain_Specific/` | Domain-specific | Monte Carlo, FDTD, optical flow, sobel |
| `cpp/6_Performance/` | Performance | occupancy, memory bandwidth analysis |
| `cpp/7_libNVVM/` | libNVVM | NVVM IR compilation |
| `cpp/8_Platform_Specific/` | Platform-specific | Windows/Linux specific integrations |
| `cpp/9_CUDA_Tile/` | C++ tile API | `cuda::tile` programming model |
| `Common/` | Shared headers | `helper_cuda.h`, `helper_math.h`, timers |

## Build

CUDA samples require the CUDA Toolkit (`nvcc`) and a CUDA-capable GPU. Upstream
CMake support is preserved in the source layout; individual samples can be built
with:

```bash
nvcc -arch=sm_90 -o vectorAdd cpp/0_Introduction/vectorAdd/vectorAdd.cu -I Common
```

Lower-level companions live in `28_ptx/` (PTX) and `29_sass/` (SASS).
