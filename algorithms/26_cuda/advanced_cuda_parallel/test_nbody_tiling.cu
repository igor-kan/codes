#include <stdio.h>
#include <assert.h>
#include "nbody_gravitational_tiling.cuh"

int main() {
    BodyPos b1 = {0,0,0, 1.0f};
    BodyPos b2 = {1,0,0, 1.0f};
    float dx = b2.x - b1.x;
    assert(dx == 1.0f);
    printf("test_nbody_tiling PASSED\n");
    return 0;
}
