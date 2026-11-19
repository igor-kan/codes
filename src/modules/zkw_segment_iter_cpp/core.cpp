#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_zkw_segment_iter_cpp {

ZkwSegTree::ZkwSegTree(int n) {
    base_ = 1;
    while (base_ < n + 2) base_ <<= 1;
    tree_.assign(2 * base_, 0);
}
void ZkwSegTree::point_set(int idx, std::int64_t val) {
    int p = idx + 1 + base_;
    tree_[p] = val;
    for (p >>= 1; p > 0; p >>= 1) tree_[p] = tree_[p << 1] + tree_[p << 1 | 1];
}
std::int64_t ZkwSegTree::range_sum(int l, int r) const {
    std::int64_t ans = 0;
    for (int s = l + base_, t = r + 2 + base_; s ^ t ^ 1; s >>= 1, t >>= 1) {
        if (~s & 1) ans += tree_[s ^ 1];
        if ( t & 1) ans += tree_[t ^ 1];
    }
    return ans;
}

} // namespace codes_zkw_segment_iter_cpp
