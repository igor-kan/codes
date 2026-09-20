#pragma once
#include <cuda_runtime.h>

__global__ void wave_equation_fdtd_2d_kernel(
    const float* __restrict__ u_prev,
    const float* __restrict__ u_curr,
    float* __restrict__ u_next,
    int nx, int ny,
    float c_sq_dt_sq_dx_sq
);
