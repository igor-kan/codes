#include "prefix_sum_scan.cuh"

__global__ void blelloch_scan_kernel(int* d_out, const int* d_in, int n) {
    extern __shared__ int temp[];
    int thid = threadIdx.x;
    int offset = 1;
    
    temp[2*thid] = (2*thid < n) ? d_in[2*thid] : 0;
    temp[2*thid+1] = (2*thid+1 < n) ? d_in[2*thid+1] : 0;
    
    for (int d = n>>1; d > 0; d >>= 1) {
        __syncthreads();
        if (thid < d) {
            int ai = offset*(2*thid+1)-1;
            int bi = offset*(2*thid+2)-1;
            temp[bi] += temp[ai];
        }
        offset *= 2;
    }
    if (thid == 0) temp[n - 1] = 0;
    for (int d = 1; d < n; d *= 2) {
        offset >>= 1;
        __syncthreads();
        if (thid < d) {
            int ai = offset*(2*thid+1)-1;
            int bi = offset*(2*thid+2)-1;
            int t = temp[ai];
            temp[ai] = temp[bi];
            temp[bi] += t;
        }
    }
    __syncthreads();
    if (2*thid < n) d_out[2*thid] = temp[2*thid];
    if (2*thid+1 < n) d_out[2*thid+1] = temp[2*thid+1];
}
