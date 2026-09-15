/* Segmented sieve of Eratosthenes. */
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

int main(void) {
    int low = 10, high = 30;
    bool segment[64];
    for (int i = 0; i <= high - low; i++) segment[i] = true;
    for (int p = 2; (long)p * p <= high; p++) {
        int start = p * p > low ? p * p : (low + p - 1) / p * p;
        for (int value = start; value <= high; value += p) segment[value - low] = false;
    }
    if (low <= 1) segment[0] = false;
    int expected[] = {11, 13, 17, 19, 23, 29};
    int index = 0;
    for (int i = 0; i <= high - low; i++)
        if (segment[i]) {
            if (low + i != expected[index++]) return 1;
        }
    if (index != 6) return 1;
    printf("segmented sieve ok\n");
    return 0;
}
