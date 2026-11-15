#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <unordered_map>

namespace codes_mo_offline_queries {
std::vector<std::size_t> answer_distinct_queries(const std::vector<int>& arr, const std::vector<RangeQuery>& queries) {
    std::vector<std::size_t> ans(queries.size(), 0);
    if (arr.empty() || queries.empty()) return ans;
    // Coordinate compress values to dense [0..U-1] ids for O(1) vector indexing!
    std::vector<int> vals = arr;
    std::sort(vals.begin(), vals.end());
    vals.erase(std::unique(vals.begin(), vals.end()), vals.end());
    std::vector<std::size_t> dense(arr.size());
    for (std::size_t i = 0; i < arr.size(); ++i) {
        dense[i] = static_cast<std::size_t>(std::lower_bound(vals.begin(), vals.end(), arr[i]) - vals.begin());
    }
    const std::size_t bsize = std::max<std::size_t>(1, static_cast<std::size_t>(std::sqrt(arr.size())));
    std::vector<RangeQuery> q = queries;
    std::sort(q.begin(), q.end(), [&](const RangeQuery& a, const RangeQuery& b) {
        std::size_t ba = a.l / bsize, bb = b.l / bsize;
        if (ba != bb) return ba < bb;
        return (ba & 1U) ? (a.r > b.r) : (a.r < b.r);
    });
    std::vector<std::size_t> freq(vals.size(), 0);
    std::size_t distinct = 0, cur_l = 0, cur_r = 0;
    auto add = [&](std::size_t idx) { if (++freq[dense[idx]] == 1) distinct++; };
    auto rem = [&](std::size_t idx) { if (--freq[dense[idx]] == 0) distinct--; };
    for (const auto& qr : q) {
        while (cur_r <= qr.r) add(cur_r++);
        while (cur_l > qr.l) add(--cur_l);
        while (cur_r > qr.r + 1) rem(--cur_r);
        while (cur_l < qr.l) rem(cur_l++);
        ans[qr.id] = distinct;
    }
    return ans;
}
} // namespace codes_mo_offline_queries
