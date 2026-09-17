#include <stdio.h>
#include <assert.h>
void combSort(int* arr, int n) {
    int gap = n, sorted = 0;
    while (!sorted) {
        gap = (int)(gap / 1.3);
        if (gap <= 1) { gap = 1; sorted = 1; }
        for (int i = 0; i + gap < n; i++) {
            if (arr[i] > arr[i + gap]) {
                int t = arr[i]; arr[i] = arr[i + gap]; arr[i + gap] = t;
                sorted = 0;
            }
        }
    }
}
int main(void) {
    int a[] = {8, 4, 1, 56, 3};
    combSort(a, 5);
    assert(a[0] == 1 && a[4] == 56);
    printf("C Comb Sort verified.\n");
    return 0;
}
