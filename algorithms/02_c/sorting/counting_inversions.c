/* Count inversions with a modified merge sort (CLRS 2.4 style). */
#include <assert.h>
#include <stdio.h>
#include <string.h>

static long merge_count(int *a, int *buf, int lo, int hi) {
    if (hi - lo <= 1) return 0;
    int mid = (lo + hi) / 2;
    long inversions = merge_count(a, buf, lo, mid) + merge_count(a, buf, mid, hi);
    int i = lo, j = mid, k = lo;
    while (i < mid && j < hi) {
        if (a[i] <= a[j]) buf[k++] = a[i++];
        else { buf[k++] = a[j++]; inversions += mid - i; }
    }
    while (i < mid) buf[k++] = a[i++];
    while (j < hi) buf[k++] = a[j++];
    memcpy(a + lo, buf + lo, (size_t)(hi - lo) * sizeof(int));
    return inversions;
}

static long count_inversions(int *a, int n) {
    int buf[64];
    return merge_count(a, buf, 0, n);
}

int main(void) {
    int a[5] = {2, 4, 1, 3, 5};
    int b[5] = {5, 4, 3, 2, 1};
    assert(count_inversions(a, 5) == 3);
    assert(count_inversions(b, 5) == 10);
    printf("counting inversions ok\n");
    return 0;
}
