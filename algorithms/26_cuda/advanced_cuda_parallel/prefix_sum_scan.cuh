#ifndef PREFIX_SUM_SCAN_CUH
#define PREFIX_SUM_SCAN_CUH

__global__ void blelloch_scan_kernel(int* d_out, const int* d_in, int n);

#endif
