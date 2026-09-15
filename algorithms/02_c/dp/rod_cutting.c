/* Rod cutting (CLRS 15.1). */
#include <assert.h>
#include <stdio.h>

static int maxi(int a, int b) { return a > b ? a : b; }

static int cut_rod(const int *prices, int n) {
    int best[64] = {0};
    for (int len = 1; len <= n; ++len)
        for (int i = 1; i <= len; ++i)
            best[len] = maxi(best[len], prices[i - 1] + best[len - i]);
    return best[n];
}

int main(void) {
    int prices[10] = {1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
    assert(cut_rod(prices, 4) == 10);
    assert(cut_rod(prices, 7) == 18);
    assert(cut_rod(prices, 10) == 30);
    printf("rod cutting ok\n");
    return 0;
}
