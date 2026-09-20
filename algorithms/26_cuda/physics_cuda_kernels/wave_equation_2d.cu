#include "wave_equation_2d.cuh"

__global__ void wave_equation_fdtd_2d_kernel(
    const float* __restrict__ u_prev,
    const float* __restrict__ u_curr,
    float* __restrict__ u_next,
    int nx, int ny,
    float c_sq_dt_sq_dx_sq
) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x <= 0 || x >= nx - 1 || y <= 0 || y >= ny - 1) return;

    int idx = y * nx + x;
    float u_c = u_curr[idx];
    float lap = u_curr[idx + 1] + u_curr[idx - 1] + u_curr[idx + nx] + u_curr[idx - nx] - 4.0f * u_c;
    u_next[idx] = 2.0f * u_c - u_prev[idx] + c_sq_dt_sq_dx_sq * lap;
}
