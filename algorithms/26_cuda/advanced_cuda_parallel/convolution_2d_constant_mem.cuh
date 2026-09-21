#ifndef CONVOLUTION_2D_CONSTANT_MEM_CUH
#define CONVOLUTION_2D_CONSTANT_MEM_CUH

#define KERNEL_RADIUS 1
#define KERNEL_W (2 * KERNEL_RADIUS + 1)

__global__ void conv2d_constant_kernel(const float* d_in, float* d_out, int width, int height);

#endif
