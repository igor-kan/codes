#include "radix_sort_gpu.cuh"

__global__ void radix_sort_pass(unsigned int* d_out, const unsigned int* d_in, int n, int bit) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n) {
        unsigned int val = d_in[idx];
        d_out[idx] = val; // placeholder for local 1-bit scan scatter
    }
}
