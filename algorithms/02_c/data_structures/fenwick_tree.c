/* Fenwick tree: point add and prefix sum. */
#include <stdio.h>

#define N 8
static int tree[N + 1];

void fenwick_add(int index, int delta) {
    for (index += 1; index <= N; index += index & -index) tree[index] += delta;
}

int fenwick_sum(int index) {
    int total = 0;
    for (index += 1; index > 0; index -= index & -index) total += tree[index];
    return total;
}

int main(void) {
    int values[N] = {1, 3, 5, 7, 9, 11, 13, 15};
    for (int i = 0; i < N; i++) fenwick_add(i, values[i]);
    if (fenwick_sum(3) != 16) return 1;
    if (fenwick_sum(N - 1) != 64) return 1;
    printf("prefix_sum(3)=%d total=%d\n", fenwick_sum(3), fenwick_sum(N - 1));
    return 0;
}
