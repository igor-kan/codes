#pragma once
#include <cuda_runtime.h>

__global__ void warp_shuffle_reduction_sum(
    const float* __restrict__ input,
    float* __restrict__ block_sums,
    int n
);
