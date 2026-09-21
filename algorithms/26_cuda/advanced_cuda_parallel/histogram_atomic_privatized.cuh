#ifndef HISTOGRAM_ATOMIC_PRIVATIZED_CUH
#define HISTOGRAM_ATOMIC_PRIVATIZED_CUH

#define NUM_BINS 256

__global__ void histogram_privatized_kernel(const unsigned char* d_data, unsigned int* d_histo, int n);

#endif
