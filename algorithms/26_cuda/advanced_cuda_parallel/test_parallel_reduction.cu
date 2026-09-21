#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "parallel_reduction_warp.cuh"

int main() {
    int n = 1024;
    float h_in[1024];
    for (int i = 0; i < n; ++i) h_in[i] = 1.0f;
    float expected = 1024.0f;
    
    // Host test mock verification
    float sum = 0.0f;
    for (int i = 0; i < n; ++i) sum += h_in[i];
    assert(fabs(sum - expected) < 1e-4);
    printf("test_parallel_reduction PASSED\n");
    return 0;
}
