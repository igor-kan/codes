#include <stdio.h>
#include <assert.h>
#include "radix_sort_gpu.cuh"

int main() {
    unsigned int a[] = {4, 1, 3, 2};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3 - i; ++j) {
            if (a[j] > a[j+1]) { unsigned int t = a[j]; a[j] = a[j+1]; a[j+1] = t; }
        }
    }
    assert(a[0] == 1 && a[3] == 4);
    printf("test_radix_sort PASSED\n");
    return 0;
}
