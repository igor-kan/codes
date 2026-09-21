#ifndef PARALLEL_REDUCTION_WARP_CUH
#define PARALLEL_REDUCTION_WARP_CUH

__global__ void warp_reduce_sum_kernel(const float* d_in, float* d_out, int n);

#endif
