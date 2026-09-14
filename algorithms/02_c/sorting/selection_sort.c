#include <stdio.h>

void selection_sort(int *a, int n) {
    for (int i = 0; i < n - 1; ++i) {
        int min_idx = i;
        for (int j = i + 1; j < n; ++j)
            if (a[j] < a[min_idx]) min_idx = j;
        int t = a[i]; a[i] = a[min_idx]; a[min_idx] = t;
    }
}

int main(void) {
    int data[] = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19};
    int n = sizeof(data) / sizeof(data[0]);
    selection_sort(data, n);
    for (int i = 1; i < n; ++i) {
        if (data[i - 1] > data[i]) {
            printf("[C SelectionSort] FAILED: not sorted at index %d\n", i);
            return 1;
        }
    }
    printf("[C SelectionSort] Selection sort verified: {");
    for (int i = 0; i < n; ++i) printf("%d%s", data[i], i + 1 < n ? ", " : "}\n");
    return 0;
}
