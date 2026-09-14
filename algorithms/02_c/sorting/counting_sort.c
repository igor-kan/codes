#include <stdio.h>
#include <string.h>

#define MAXV 1000000

void counting_sort(int *a, int n, int max_val) {
    int count[MAXV + 1];
    memset(count, 0, (max_val + 1) * sizeof(int));
    for (int i = 0; i < n; ++i) ++count[a[i]];
    int idx = 0;
    for (int v = 0; v <= max_val; ++v)
        while (count[v]-- > 0) a[idx++] = v;
}

int main(void) {
    int data[] = {5, 3, 8, 1, 9, 2, 7, 4, 6, 0};
    int n = sizeof(data) / sizeof(data[0]);
    counting_sort(data, n, 9);
    for (int i = 1; i < n; ++i) {
        if (data[i - 1] > data[i]) {
            printf("[C CountingSort] FAILED: not sorted at index %d\n", i);
            return 1;
        }
    }
    printf("[C CountingSort] Counting sort verified: {");
    for (int i = 0; i < n; ++i) printf("%d%s", data[i], i + 1 < n ? ", " : "}\n");
    return 0;
}
