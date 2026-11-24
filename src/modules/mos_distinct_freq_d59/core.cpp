#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_mos_distinct_freq_d59 {

std::vector<long long> count_equal_pairs_queries(const std::vector<int>& xs, const std::vector<std::pair<int, int>>& qs) {
    int n = static_cast<int>(xs.size());
    int blk = std::max(1, static_cast<int>(std::sqrt(static_cast<double>(n))));
    struct Q { int l, r, idx; };
    std::vector<Q> ord;
    for (int i = 0; i < static_cast<int>(qs.size()); ++i) ord.push_back({qs[i].first, qs[i].second, i});
    std::sort(ord.begin(), ord.end(), [&](const Q& a, const Q& b) {
        int ba = a.l / blk, bb = b.l / blk;
        if (ba != bb) return ba < bb;
        return (ba & 1) ? (a.r > b.r) : (a.r < b.r);
    });
    int mx = *std::max_element(xs.begin(), xs.end());
    std::vector<long long> freq(mx + 1, 0), ans(qs.size(), 0);
    long long cur = 0;
    auto add = [&](int p) { cur += freq[xs[p]]; ++freq[xs[p]]; };
    auto rem = [&](int p) { --freq[xs[p]]; cur -= freq[xs[p]]; };
    int cl = 0, cr = -1;
    for (const auto& q : ord) {
        while (cr < q.r) add(++cr);
        while (cl > q.l) add(--cl);
        while (cr > q.r) rem(cr--);
        while (cl < q.l) rem(cl++);
        ans[q.idx] = cur;
    }
    return ans;
}

} // namespace codes_mos_distinct_freq_d59
