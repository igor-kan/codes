#include "prefix_sum_scan.cuh"

__global__ void blelloch_work_efficient_scan(float* d_out, const float* d_in, int n) {
    extern __shared__ float temp[];
    int thid = threadIdx.x;
    int offset = 1;

    int ai = thid;
    int bi = thid + (n / 2);
    temp[2 * thid] = (2 * thid < n) ? d_in[2 * thid] : 0.0f;
    temp[2 * thid + 1] = (2 * thid + 1 < n) ? d_in[2 * thid + 1] : 0.0f;

    // Up-sweep (reduce)
    for (int d = n >> 1; d > 0; d >>= 1) {
        __syncthreads();
        if (thid < d) {
            int i1 = offset * (2 * thid + 1) - 1;
            int i2 = offset * (2 * thid + 2) - 1;
            temp[i2] += temp[i1];
        }
        offset *= 2;
    }

    if (thid == 0) temp[n - 1] = 0.0f; // Clear root

    // Down-sweep
    for (int d = 1; d < n; d *= 2) {
        offset >>= 1;
        __syncthreads();
        if (thid < d) {
            int i1 = offset * (2 * thid + 1) - 1;
            int i2 = offset * (2 * thid + 2) - 1;
            float t = temp[i1];
            temp[i1] = temp[i2];
            temp[i2] += t;
        }
    }
    __syncthreads();

    if (2 * thid < n) d_out[2 * thid] = temp[2 * thid];
    if (2 * thid + 1 < n) d_out[2 * thid + 1] = temp[2 * thid + 1];
}
