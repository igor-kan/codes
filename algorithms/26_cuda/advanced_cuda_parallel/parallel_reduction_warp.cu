#include "parallel_reduction_warp.cuh"

__inline__ __device__ float warp_reduce(float val) {
    for (int offset = 16; offset > 0; offset /= 2) {
        val += __shfl_down_sync(0xffffffff, val, offset);
    }
    return val;
}

__global__ void warp_reduce_sum_kernel(const float* d_in, float* d_out, int n) {
    int tid = threadIdx.x;
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    float sum = (idx < n) ? d_in[idx] : 0.0f;
    sum = warp_reduce(sum);
    if ((tid % 32) == 0) {
        atomicAdd(d_out, sum);
    }
}
