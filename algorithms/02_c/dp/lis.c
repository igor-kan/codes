#include <stdio.h>

#define MAXN 100000

int lis_length(const int *a, int n) {
    int tails[MAXN], len = 0;
    for (int i = 0; i < n; ++i) {
        int lo = 0, hi = len;
        while (lo < hi) {
            int m = (lo + hi) / 2;
            if (tails[m] < a[i]) lo = m + 1;
            else hi = m;
        }
        tails[lo] = a[i];
        if (lo == len) ++len;
    }
    return len;
}

int main(void) {
    int a[] = {10, 9, 2, 5, 3, 7, 101, 18};
    int n = sizeof(a) / sizeof(a[0]);

    if (lis_length(a, n) != 4) {
        printf("[C LIS] FAILED: length %d, want 4\n", lis_length(a, n));
        return 1;
    }
    printf("[C LIS] Longest increasing subsequence verified (O(n log n))\n");
    return 0;
}
