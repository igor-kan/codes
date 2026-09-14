#include <stdio.h>

int max_subarray_sum(const int *a, int n, int k) {
    int sum = 0;
    for (int i = 0; i < k; ++i) sum += a[i];
    int best = sum;
    for (int i = k; i < n; ++i) {
        sum += a[i] - a[i - k];
        if (sum > best) best = sum;
    }
    return best;
}

int main(void) {
    int a[] = {1, 4, 2, 10, 23, 3, 1, 0, 20};
    int n = sizeof(a) / sizeof(a[0]);

    if (max_subarray_sum(a, n, 4) != 39) {
        printf("[C SlidingWindow] FAILED: max fixed-window sum\n");
        return 1;
    }
    printf("[C SlidingWindow] Fixed-size window max sum verified\n");
    return 0;
}
