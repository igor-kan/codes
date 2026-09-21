#ifndef RADIX_SORT_GPU_CUH
#define RADIX_SORT_GPU_CUH

__global__ void radix_sort_pass(unsigned int* d_out, const unsigned int* d_in, int n, int bit);

#endif
