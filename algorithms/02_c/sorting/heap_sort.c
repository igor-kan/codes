#include <stdio.h>
#include <stdlib.h>

static void sift_down(int *a, int start, int end) {
    int root = start;
    while (root * 2 + 1 <= end) {
        int child = root * 2 + 1;
        int swap = root;
        if (a[swap] < a[child]) swap = child;
        if (child + 1 <= end && a[swap] < a[child + 1]) swap = child + 1;
        if (swap == root) return;
        int tmp = a[root]; a[root] = a[swap]; a[swap] = tmp;
        root = swap;
    }
}

void heap_sort(int *a, int n) {
    for (int start = (n - 2) / 2; start >= 0; --start)
        sift_down(a, start, n - 1);
    for (int end = n - 1; end > 0; --end) {
        int tmp = a[end]; a[end] = a[0]; a[0] = tmp;
        sift_down(a, 0, end - 1);
    }
}

int main(void) {
    int data[] = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19};
    int n = sizeof(data) / sizeof(data[0]);
    heap_sort(data, n);
    for (int i = 1; i < n; ++i) {
        if (data[i - 1] > data[i]) {
            printf("[C HeapSort] FAILED: not sorted at index %d\n", i);
            return 1;
        }
    }
    printf("[C HeapSort] Sift-down heap sort verified: {");
    for (int i = 0; i < n; ++i) printf("%d%s", data[i], i + 1 < n ? ", " : "}\n");
    return 0;
}
