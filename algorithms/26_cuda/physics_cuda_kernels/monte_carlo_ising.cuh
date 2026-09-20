#pragma once
#include <cuda_runtime.h>

__global__ void ising_checkerboard_sweep_kernel(
    int8_t* lattice,
    int L,
    float beta,
    int color, // 0 for black, 1 for white
    unsigned long long seed
);
