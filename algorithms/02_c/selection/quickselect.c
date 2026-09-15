/* Quickselect: expected linear-time order statistic (CLRS 9.2). */
#include <assert.h>
#include <stdio.h>

static int quickselect(int *a, int n, int k) {
    int lo = 0, hi = n - 1;
    while (1) {
        int pivot = a[hi], i = lo, j;
        for (j = lo; j < hi; ++j) {
            if (a[j] < pivot) {
                int t = a[i]; a[i++] = a[j]; a[j] = t;
            }
        }
        int t = a[i]; a[i] = a[hi]; a[hi] = t;
        if (i == k) return a[i];
        if (k < i) hi = i - 1; else lo = i + 1;
    }
}

int main(void) {
    int data[6] = {3, 2, 1, 5, 6, 4};
    int expected[6] = {1, 2, 3, 4, 5, 6};
    for (int k = 0; k < 6; ++k) {
        int copy[6];
        for (int i = 0; i < 6; ++i) copy[i] = data[i];
        assert(quickselect(copy, 6, k) == expected[k]);
    }
    printf("quickselect ok\n");
    return 0;
}
