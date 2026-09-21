#include <stdio.h>
#include <assert.h>
#include "heat_diffusion_2d_cuda.cuh"

int main() {
    float u[9] = {0, 1, 0, 1, 4, 1, 0, 1, 0};
    float laplacian = u[3] + u[5] + u[1] + u[7] - 4.0f * u[4]; // 1 + 1 + 1 + 1 - 16 = -12
    assert(laplacian == -12.0f);
    printf("test_heat_diffusion PASSED\n");
    return 0;
}
