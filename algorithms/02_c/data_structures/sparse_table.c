#include <stdio.h>

#define MAXN 100000
#define LOG 17

static int st[LOG][MAXN];
static int lg[MAXN + 1];

static int min2(int a, int b) { return a < b ? a : b; }

void sparse_build(const int *a, int n) {
    for (int i = 0; i < n; ++i) st[0][i] = a[i];
    for (int k = 1; (1 << k) <= n; ++k)
        for (int i = 0; i + (1 << k) <= n; ++i)
            st[k][i] = min2(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
    lg[1] = 0;
    for (int i = 2; i <= n; ++i) lg[i] = lg[i / 2] + 1;
}

int sparse_query(int l, int r) {
    int k = lg[r - l + 1];
    return min2(st[k][l], st[k][r - (1 << k) + 1]);
}

int main(void) {
    int a[] = {5, 2, 4, 7, 1, 8, 3};
    int n = sizeof(a) / sizeof(a[0]);
    sparse_build(a, n);

    if (sparse_query(0, 6) != 1 || sparse_query(0, 2) != 2 || sparse_query(3, 5) != 1) {
        printf("[C SparseTable] FAILED: RMQ mismatch\n");
        return 1;
    }
    printf("[C SparseTable] O(1) range minimum query verified\n");
    return 0;
}
