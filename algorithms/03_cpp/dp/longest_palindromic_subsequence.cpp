/**
 * Longest Palindromic Subsequence via interval DP.
 */

#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

int lps(const std::string& s) {
    int n = static_cast<int>(s.size());
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
    for (int i = 0; i < n; ++i) dp[i][i] = 1;
    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            if (s[i] == s[j]) dp[i][j] = dp[i + 1][j - 1] + 2;
            else dp[i][j] = std::max(dp[i + 1][j], dp[i][j - 1]);
        }
    }
    return dp[0][n - 1];
}

int main() {
    assert(lps("bbbab") == 4);
    assert(lps("cbbd") == 2);
    assert(lps("a") == 1);
    assert(lps("racecar") == 7);
    std::cout << "[C++ LPS] Longest palindromic subsequence verified." << std::endl;
    return 0;
}
