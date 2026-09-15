/* Reservoir sampling for a uniform sample of a stream (CLRS 5.3). */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    srand(42);
    int k = 5, n = 100, reservoir[5], count = 0;
    for (int i = 0; i < n; ++i) {
        if (i < k) reservoir[count++] = i;
        else {
            int j = rand() % (i + 1);
            if (j < k) reservoir[j] = i;
        }
    }
    assert(count == k);
    printf("reservoir sampling ok\n");
    return 0;
}
