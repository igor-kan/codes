#ifndef HEAT_DIFFUSION_2D_CUDA_CUH
#define HEAT_DIFFUSION_2D_CUDA_CUH

__global__ void heat_diff_2d_kernel(const float* d_u, float* d_unext, int nx, int ny, float alpha_dt_dx2);

#endif
