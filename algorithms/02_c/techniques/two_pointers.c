#include <stdio.h>

int two_sum(const int *a, int n, int target) {
    int l = 0, r = n - 1;
    while (l < r) {
        int s = a[l] + a[r];
        if (s == target) return 1;
        if (s < target) ++l;
        else --r;
    }
    return 0;
}

int main(void) {
    int a[] = {1, 2, 3, 4, 6};
    int n = sizeof(a) / sizeof(a[0]);

    if (!two_sum(a, n, 6)) {
        printf("[C TwoPointers] FAILED: existing pair 2+4\n");
        return 1;
    }
    if (two_sum(a, n, 12)) {
        printf("[C TwoPointers] FAILED: phantom pair\n");
        return 1;
    }
    printf("[C TwoPointers] Two-sum on sorted array verified\n");
    return 0;
}
