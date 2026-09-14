/* LSD radix sort for non-negative ints. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void counting_pass(int *a, int n, int exp) {
    int *out = malloc((size_t)n * sizeof(int));
    int count[10] = {0};
    for (int i = 0; i < n; i++) count[(a[i] / exp) % 10]++;
    for (int i = 1; i < 10; i++) count[i] += count[i - 1];
    for (int i = n - 1; i >= 0; i--) {
        int digit = (a[i] / exp) % 10;
        out[--count[digit]] = a[i];
    }
    memcpy(a, out, (size_t)n * sizeof(int));
    free(out);
}

void radix_sort(int *a, int n) {
    int max = a[0];
    for (int i = 1; i < n; i++) if (a[i] > max) max = a[i];
    for (int exp = 1; max / exp > 0; exp *= 10) counting_pass(a, n, exp);
}

int main(void) {
    int a[] = {170, 45, 75, 90, 802, 24, 2, 66};
    int n = (int)(sizeof(a) / sizeof(a[0]));
    radix_sort(a, n);
    for (int i = 1; i < n; i++) if (a[i - 1] > a[i]) return 1;
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
