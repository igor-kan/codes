#include "convolution_2d_constant_mem.cuh"

__constant__ float d_Kernel[KERNEL_W * KERNEL_W];

__global__ void conv2d_constant_kernel(const float* d_in, float* d_out, int width, int height) {
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    
    if (col < width && row < height) {
        float sum = 0.0f;
        for (int r = -KERNEL_RADIUS; r <= KERNEL_RADIUS; ++r) {
            for (int c = -KERNEL_RADIUS; c <= KERNEL_RADIUS; ++c) {
                int cur_row = row + r;
                int cur_col = col + c;
                if (cur_row >= 0 && cur_row < height && cur_col >= 0 && cur_col < width) {
                    sum += d_in[cur_row * width + cur_col] * d_Kernel[(r + KERNEL_RADIUS)*KERNEL_W + (c + KERNEL_RADIUS)];
                }
            }
        }
        d_out[row * width + col] = sum;
    }
}
