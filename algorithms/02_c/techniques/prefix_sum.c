#include <stdio.h>

#define MAXN 100000

void prefix_build(const int *a, int n, long long *pref) {
    pref[0] = 0;
    for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + a[i];
}

long long prefix_range(const long long *pref, int l, int r) {
    return pref[r + 1] - pref[l];
}

int main(void) {
    int a[] = {1, 2, 3, 4, 5};
    int n = sizeof(a) / sizeof(a[0]);
    long long pref[MAXN + 1];

    prefix_build(a, n, pref);
    if (prefix_range(pref, 0, 4) != 15 || prefix_range(pref, 1, 3) != 9 || prefix_range(pref, 2, 2) != 3) {
        printf("[C PrefixSum] FAILED: range sum mismatch\n");
        return 1;
    }
    printf("[C PrefixSum] Prefix sum range queries verified\n");
    return 0;
}
