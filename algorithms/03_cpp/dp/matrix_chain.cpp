/**
 * Matrix chain multiplication: minimum scalar multiplications.
 */

#include <vector>
#include <algorithm>
#include <climits>
#include <cassert>
#include <iostream>

int matrixChain(const std::vector<int>& dims) {
    int n = static_cast<int>(dims.size()) - 1; // number of matrices
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; ++k) {
                int cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1];
                dp[i][j] = std::min(dp[i][j], cost);
            }
        }
    }
    return dp[0][n - 1];
}

int main() {
    assert(matrixChain({10, 20, 30, 40, 30}) == 30000);
    assert(matrixChain({1, 2, 3, 4}) == 18);
    assert(matrixChain({5, 4}) == 0);
    std::cout << "[C++ MatrixChain] Minimum multiplication count verified." << std::endl;
    return 0;
}
