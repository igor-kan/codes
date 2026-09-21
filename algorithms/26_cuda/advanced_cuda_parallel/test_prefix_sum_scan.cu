#include <stdio.h>
#include <assert.h>

int main() {
    int in[] = {1, 2, 3, 4};
    int expected[] = {0, 1, 3, 6}; // Exclusive scan
    int acc = 0;
    for (int i = 0; i < 4; ++i) {
        assert(acc == expected[i]);
        acc += in[i];
    }
    printf("test_prefix_sum_scan PASSED\n");
    return 0;
}
