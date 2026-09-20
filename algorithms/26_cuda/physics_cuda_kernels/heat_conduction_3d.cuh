#pragma once
#include <cuda_runtime.h>

__global__ void heat_conduction_3d_kernel(
    const float* __restrict__ T_curr,
    float* __restrict__ T_next,
    int nx, int ny, int nz,
    float alpha_dt_dx_sq
);
