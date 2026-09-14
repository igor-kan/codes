#include <stdio.h>

void insertion_sort(int *a, int n) {
    for (int i = 1; i < n; ++i) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            --j;
        }
        a[j + 1] = key;
    }
}

int main(void) {
    int data[] = {33, 7, 91, 12, 5, 5, 78, 2, 44, 19};
    int n = sizeof(data) / sizeof(data[0]);
    insertion_sort(data, n);
    for (int i = 1; i < n; ++i) {
        if (data[i - 1] > data[i]) {
            printf("[C InsertionSort] FAILED: not sorted at index %d\n", i);
            return 1;
        }
    }
    printf("[C InsertionSort] Insertion sort verified: {");
    for (int i = 0; i < n; ++i) printf("%d%s", data[i], i + 1 < n ? ", " : "}\n");
    return 0;
}
