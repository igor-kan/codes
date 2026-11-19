#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_mo_tree_hilbert_order {

std::uint64_t hilbert_order(int x, int y, int pow2_log) {
    std::uint64_t d = 0;
    for (int s = 1 << (pow2_log - 1); s > 0; s >>= 1) {
        int rx = (x & s) > 0, ry = (y & s) > 0;
        d += static_cast<std::uint64_t>(s) * s * ((3 * rx) ^ ry);
        if (ry == 0) {
            if (rx == 1) { x = (1 << pow2_log) - 1 - x; y = (1 << pow2_log) - 1 - y; }
            std::swap(x, y);
        }
    }
    return d;
}
std::vector<int> mo_distinct_queries(const std::vector<int>& arr, const std::vector<std::pair<int, int>>& qs) {
    std::vector<MoQuery> items;
    items.reserve(qs.size());
    for (int i = 0; i < static_cast<int>(qs.size()); ++i) {
        items.push_back({qs[i].first, qs[i].second, i, hilbert_order(qs[i].first, qs[i].second, 10)});
    }
    std::sort(items.begin(), items.end(), [](const MoQuery& a, const MoQuery& b) { return a.h_ord < b.h_ord; });
    int mx = arr.empty() ? 0 : *std::max_element(arr.begin(), arr.end());
    std::vector<int> freq(mx + 1, 0), ans(qs.size(), 0);
    int cur_l = 0, cur_r = -1, distinct = 0;
    auto add = [&](int idx) { if (++freq[arr[idx]] == 1) ++distinct; };
    auto rem = [&](int idx) { if (--freq[arr[idx]] == 0) --distinct; };
    for (const auto& q : items) {
        while (cur_l > q.l) add(--cur_l);
        while (cur_r < q.r) add(++cur_r);
        while (cur_l < q.l) rem(cur_l++);
        while (cur_r > q.r) rem(cur_r--);
        ans[q.id] = distinct;
    }
    return ans;
}

} // namespace codes_mo_tree_hilbert_order
