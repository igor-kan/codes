/* Catalan numbers by the recurrence. */
#include <stdio.h>
int main(void) {
    long c[11] = {0};
    c[0] = 1;
    for (int i = 1; i <= 10; i++) {
        long s = 0;
        for (int j = 0; j < i; j++) s += c[j] * c[i - 1 - j];
        c[i] = s;
    }
    if (c[5] != 42 || c[10] != 16796) return 1;
    printf("catalan(10)=%ld\n", c[10]);
    return 0;
}
