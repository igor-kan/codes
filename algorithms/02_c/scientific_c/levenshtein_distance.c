#include "levenshtein_distance.h"
#include <string.h>
#include <stdlib.h>

int levenshtein(const char *s1, const char *s2) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    int *dp = (int *)malloc((len2 + 1) * sizeof(int));
    
    for (int j = 0; j <= len2; ++j) dp[j] = j;
    
    for (int i = 1; i <= len1; ++i) {
        int prev = dp[0];
        dp[0] = i;
        for (int j = 1; j <= len2; ++j) {
            int temp = dp[j];
            int cost = (s1[i - 1] == s2[j - 1]) ? 0 : 1;
            int ins = dp[j] + 1;
            int del = dp[j - 1] + 1;
            int sub = prev + cost;
            int min_val = (ins < del) ? ins : del;
            dp[j] = (min_val < sub) ? min_val : sub;
            prev = temp;
        }
    }
    int res = dp[len2];
    free(dp);
    return res;
}
