#include <stdio.h>

int kadane(const int *a, int n) {
    int best = a[0], cur = a[0];
    for (int i = 1; i < n; ++i) {
        cur = (cur > 0 ? cur : 0) + a[i];
        if (cur > best) best = cur;
    }
    return best;
}

int main(void) {
    int a[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int b[] = {-1, -2, -3, -4};
    int n1 = sizeof(a) / sizeof(a[0]);
    int n2 = sizeof(b) / sizeof(b[0]);

    if (kadane(a, n1) != 6) {
        printf("[C Kadane] FAILED: max subarray sum\n");
        return 1;
    }
    if (kadane(b, n2) != -1) {
        printf("[C Kadane] FAILED: all-negative array\n");
        return 1;
    }
    printf("[C Kadane] Maximum subarray sum verified\n");
    return 0;
}
