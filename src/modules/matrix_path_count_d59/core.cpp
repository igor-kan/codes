#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_matrix_path_count_d59 {

std::vector<std::vector<long long>> count_k_walks(const std::vector<std::vector<long long>>& adj, long long k) {
    const long long MOD = 1000000007LL;
    int n = static_cast<int>(adj.size());
    auto mul = [&](const auto& a, const auto& b) {
        std::vector<std::vector<long long>> c(n, std::vector<long long>(n, 0));
        for (int i = 0; i < n; ++i) {
            for (int m = 0; m < n; ++m) {
                if (a[i][m] == 0) continue;
                for (int j = 0; j < n; ++j) c[i][j] = (c[i][j] + a[i][m] * b[m][j]) % MOD;
            }
        }
        return c;
    };
    std::vector<std::vector<long long>> res(n, std::vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    auto base = adj;
    while (k > 0) {
        if (k & 1LL) res = mul(res, base);
        base = mul(base, base);
        k >>= 1;
    }
    return res;
}

} // namespace codes_matrix_path_count_d59
