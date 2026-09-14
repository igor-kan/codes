#include <stdio.h>
#include <string.h>

#define MAX 1001

static int dp[MAX][MAX];

int longest_palindromic_subsequence(const char *s) {
    int n = strlen(s);
    for (int i = n - 1; i >= 0; --i) {
        dp[i][i] = 1;
        for (int j = i + 1; j < n; ++j) {
            if (s[i] == s[j]) dp[i][j] = dp[i + 1][j - 1] + 2;
            else dp[i][j] = dp[i + 1][j] > dp[i][j - 1] ? dp[i + 1][j] : dp[i][j - 1];
        }
    }
    return dp[0][n - 1];
}

int main(void) {
    if (longest_palindromic_subsequence("bbbab") != 4) {
        printf("[C LPS] FAILED: bbbab -> 4\n");
        return 1;
    }
    if (longest_palindromic_subsequence("cbbd") != 2) {
        printf("[C LPS] FAILED: cbbd -> 2\n");
        return 1;
    }
    printf("[C LPS] Longest palindromic subsequence verified\n");
    return 0;
}
