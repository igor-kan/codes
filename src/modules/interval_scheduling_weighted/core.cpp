#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_interval_scheduling_weighted {

long long max_non_overlapping_weight(std::vector<WeightedJob> jobs) {
    if (jobs.empty()) return 0;
    for (const auto& j : jobs) {
        if (j.end < j.start || j.weight < 0) throw std::invalid_argument("invalid job interval");
    }
    std::sort(jobs.begin(), jobs.end(), [](const WeightedJob& a, const WeightedJob& b) {
        if (a.end != b.end) return a.end < b.end;
        return a.start < b.start;
    });
    int n = static_cast<int>(jobs.size());
    std::vector<long long> ends(n);
    for (int i = 0; i < n; ++i) ends[i] = jobs[i].end;
    std::vector<long long> dp(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        auto it = std::upper_bound(ends.begin(), ends.begin() + i, jobs[i].start);
        int p = static_cast<int>(it - ends.begin());
        dp[i + 1] = std::max(dp[i], dp[p] + jobs[i].weight);
    }
    return dp[n];
}

} // namespace codes_interval_scheduling_weighted
