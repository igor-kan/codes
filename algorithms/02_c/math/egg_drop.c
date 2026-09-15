/* Egg dropping: minimum trials with k eggs and n floors. */
#include <stdio.h>
int main(void) {
    int eggs = 2, floors = 100;
    int dp[101][3] = {{0}};
    int t = 0;
    while (dp[t][eggs] < floors) {
        t++;
        for (int k = 1; k <= eggs; k++)
            dp[t][k] = dp[t - 1][k - 1] + dp[t - 1][k] + 1;
    }
    if (t != 14) return 1;
    printf("egg drop=%d\n", t);
    return 0;
}
