#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_knapsack_bounded_dp_d57 {

long long bounded_knapsack_max(int cap, const std::vector<BoundedBundle>& items) {
    if (cap < 0) throw std::invalid_argument("negative capacity");
    std::vector<long long> dp(cap + 1, 0);
    for (const auto& it : items) {
        if (it.weight <= 0 || it.count <= 0) continue;
        int rem = it.count;
        for (int k = 1; rem > 0; k <<= 1) {
            int take = std::min(k, rem);
            rem -= take;
            long long bw = static_cast<long long>(it.weight) * take;
            long long bv = it.value * take;
            if (bw > cap) continue;
            int w_int = static_cast<int>(bw);
            for (int w = cap; w >= w_int; --w) {
                dp[w] = std::max(dp[w], dp[w - w_int] + bv);
            }
        }
    }
    return dp[cap];
}

} // namespace codes_knapsack_bounded_dp_d57
