#include "histogram_atomic_privatized.cuh"

__global__ void histogram_privatized_kernel(const unsigned char* d_data, unsigned int* d_histo, int n) {
    __shared__ unsigned int histo_private[NUM_BINS];
    if (threadIdx.x < NUM_BINS) histo_private[threadIdx.x] = 0;
    __syncthreads();
    
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        atomicAdd(&(histo_private[d_data[i]]), 1);
    }
    __syncthreads();
    
    if (threadIdx.x < NUM_BINS) {
        atomicAdd(&(d_histo[threadIdx.x]), histo_private[threadIdx.x]);
    }
}
