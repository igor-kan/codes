#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_bitmask_subset_dp_d58 {

long long min_bitmask_assignment(const std::vector<std::vector<long long>>& cost) {
    int n = static_cast<int>(cost.size());
    if (n == 0 || n > 16) throw std::invalid_argument("n in 1..16 expected");
    const long long INF = 1000000000000000LL;
    int full = 1 << n;
    std::vector<long long> dp(full, INF);
    dp[0] = 0;
    for (int mask = 0; mask < full - 1; ++mask) {
        int i = 0;
        for (int b = 0; b < n; ++b) if (mask & (1 << b)) ++i;
        for (int j = 0; j < n; ++j) {
            if (!(mask & (1 << j))) {
                int nmask = mask | (1 << j);
                dp[nmask] = std::min(dp[nmask], dp[mask] + cost[i][j]);
            }
        }
    }
    return dp[full - 1];
}

} // namespace codes_bitmask_subset_dp_d58
