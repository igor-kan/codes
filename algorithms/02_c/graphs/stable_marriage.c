/* Gale-Shapley stable matching. */
#include <assert.h>
#include <stdio.h>

int main(void) {
    int men_pref[3][3] = {{0,1,2},{1,0,2},{0,1,2}};
    int women_pref[3][3] = {{2,1,0},{0,1,2},{0,1,2}};
    int n = 3, rank[3][3];
    for (int w = 0; w < n; ++w)
        for (int i = 0; i < n; ++i) rank[w][women_pref[w][i]] = i;

    int free[16], free_count = n;
    for (int m = 0; m < n; ++m) free[m] = m;
    int next[3] = {0, 0, 0}, engaged_to[3] = {-1, -1, -1};
    while (free_count > 0) {
        int m = free[--free_count];
        int w = men_pref[m][next[m]++];
        if (engaged_to[w] == -1) engaged_to[w] = m;
        else if (rank[w][m] < rank[w][engaged_to[w]]) {
            free[free_count++] = engaged_to[w];
            engaged_to[w] = m;
        } else free[free_count++] = m;
    }
    assert(engaged_to[0] == 2 && engaged_to[1] == 0 && engaged_to[2] == 1);
    printf("stable marriage ok\n");
    return 0;
}
