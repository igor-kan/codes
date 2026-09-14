#include <stdio.h>

#define MAXN 100000

void next_greater(const int *a, int n, int *nge) {
    int st[MAXN], top = -1;
    for (int i = n - 1; i >= 0; --i) {
        while (top >= 0 && st[top] <= a[i]) --top;
        nge[i] = top >= 0 ? st[top] : -1;
        st[++top] = a[i];
    }
}

int main(void) {
    int a[] = {4, 5, 2, 10, 8};
    int n = sizeof(a) / sizeof(a[0]);
    int expected[] = {5, 10, 10, -1, -1};
    int nge[MAXN];

    next_greater(a, n, nge);
    for (int i = 0; i < n; ++i) {
        if (nge[i] != expected[i]) {
            printf("[C MonotonicStack] FAILED at index %d: got %d, want %d\n", i, nge[i], expected[i]);
            return 1;
        }
    }
    printf("[C MonotonicStack] Next greater element verified\n");
    return 0;
}
