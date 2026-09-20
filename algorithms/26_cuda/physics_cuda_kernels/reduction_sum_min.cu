#include "reduction_sum_min.cuh"

__device__ float warp_reduce_sum(float val) {
    for (int offset = 16; offset > 0; offset /= 2) {
        val += __shfl_down_sync(0xFFFFFFFF, val, offset);
    }
    return val;
}

__global__ void warp_shuffle_reduction_sum(
    const float* __restrict__ input,
    float* __restrict__ block_sums,
    int n
) {
    __shared__ float warp_sums[32];
    int tid = threadIdx.x;
    int i = blockIdx.x * blockDim.x + tid;
    float sum = (i < n) ? input[i] : 0.0f;

    sum = warp_reduce_sum(sum);
    int lane = tid & 31;
    int warp_id = tid >> 5;

    if (lane == 0) {
        warp_sums[warp_id] = sum;
    }
    __syncthreads();

    float block_sum = (tid < (blockDim.x >> 5)) ? warp_sums[lane] : 0.0f;
    if (warp_id == 0) {
        block_sum = warp_reduce_sum(block_sum);
        if (lane == 0) {
            block_sums[blockIdx.x] = block_sum;
        }
    }
}
