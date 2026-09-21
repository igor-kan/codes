#include "heat_diffusion_2d_cuda.cuh"

__global__ void heat_diff_2d_kernel(const float* d_u, float* d_unext, int nx, int ny, float alpha_dt_dx2) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int j = blockIdx.y * blockDim.y + threadIdx.y;
    
    if (i > 0 && i < nx - 1 && j > 0 && j < ny - 1) {
        int idx = j * nx + i;
        float laplacian = d_u[idx - 1] + d_u[idx + 1] + d_u[idx - nx] + d_u[idx + nx] - 4.0f * d_u[idx];
        d_unext[idx] = d_u[idx] + alpha_dt_dx2 * laplacian;
    }
}
