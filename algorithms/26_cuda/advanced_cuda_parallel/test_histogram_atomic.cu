#include <stdio.h>
#include <assert.h>
#include "histogram_atomic_privatized.cuh"

int main() {
    unsigned char data[4] = {0, 1, 0, 2};
    int counts[3] = {0};
    for (int i = 0; i < 4; ++i) counts[data[i]]++;
    assert(counts[0] == 2 && counts[1] == 1 && counts[2] == 1);
    printf("test_histogram_atomic PASSED\n");
    return 0;
}
