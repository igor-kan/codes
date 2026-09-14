#include <stdio.h>

int lower_bound(const int *a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int m = (lo + hi) / 2;
        if (a[m] < x) lo = m + 1;
        else hi = m;
    }
    return lo;
}

int upper_bound(const int *a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int m = (lo + hi) / 2;
        if (a[m] <= x) lo = m + 1;
        else hi = m;
    }
    return lo;
}

int main(void) {
    int a[] = {1, 2, 2, 2, 4, 5};
    int n = sizeof(a) / sizeof(a[0]);

    if (lower_bound(a, n, 2) != 1 || lower_bound(a, n, 0) != 0 || lower_bound(a, n, 6) != n) {
        printf("[C BinarySearch] FAILED: lower_bound\n");
        return 1;
    }
    if (upper_bound(a, n, 2) != 4 || upper_bound(a, n, 5) != 6 || upper_bound(a, n, 0) != 0) {
        printf("[C BinarySearch] FAILED: upper_bound\n");
        return 1;
    }
    printf("[C BinarySearch] lower_bound / upper_bound verified\n");
    return 0;
}
