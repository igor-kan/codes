#include "heat_conduction_3d.cuh"

__global__ void heat_conduction_3d_kernel(
    const float* __restrict__ T_curr,
    float* __restrict__ T_next,
    int nx, int ny, int nz,
    float alpha_dt_dx_sq
) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;
    int z = blockIdx.z * blockDim.z + threadIdx.z;

    if (x <= 0 || x >= nx - 1 || y <= 0 || y >= ny - 1 || z <= 0 || z >= nz - 1) return;

    int idx = z * (nx * ny) + y * nx + x;
    float tc = T_curr[idx];
    float lap = (T_curr[idx + 1] + T_curr[idx - 1] +
                 T_curr[idx + nx] + T_curr[idx - nx] +
                 T_curr[idx + nx * ny] + T_curr[idx - nx * ny]) - 6.0f * tc;
    T_next[idx] = tc + alpha_dt_dx_sq * lap;
}
