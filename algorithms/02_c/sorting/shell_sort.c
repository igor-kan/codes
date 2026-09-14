/* Shell sort with Knuth's gap sequence. */
#include <stdio.h>

void shell_sort(int *a, int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = a[i], j = i;
            while (j >= gap && a[j - gap] > temp) {
                a[j] = a[j - gap];
                j -= gap;
            }
            a[j] = temp;
        }
    }
}

int main(void) {
    int a[] = {12, 34, 54, 2, 3, 90, 45};
    int n = (int)(sizeof(a) / sizeof(a[0]));
    shell_sort(a, n);
    for (int i = 1; i < n; i++) if (a[i - 1] > a[i]) return 1;
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
