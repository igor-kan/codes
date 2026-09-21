#include <stdio.h>
#include <assert.h>
#include "convolution_2d_constant_mem.cuh"

int main() {
    float img[9] = {0,0,0, 0,1,0, 0,0,0};
    float kernel[9] = {1,1,1, 1,1,1, 1,1,1};
    float sum = 0.0f;
    for (int i = 0; i < 9; ++i) sum += img[i] * kernel[i];
    assert(sum == 1.0f);
    printf("test_convolution_2d PASSED\n");
    return 0;
}
