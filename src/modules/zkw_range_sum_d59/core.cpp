#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_zkw_range_sum_d59 {

ZkwSumTree::ZkwSumTree(int n) : n_(n), t_(2 * n, 0) {}

void ZkwSumTree::add(int idx, long long delta) {
    for (t_[idx += n_] += delta; idx > 1; idx >>= 1) {
        t_[idx >> 1] = t_[idx] + t_[idx ^ 1];
    }
}

long long ZkwSumTree::sum(int l, int r) const {
    long long res = 0;
    for (l += n_, r += n_ + 1; l < r; l >>= 1, r >>= 1) {
        if (l & 1) res += t_[l++];
        if (r & 1) res += t_[--r];
    }
    return res;
}

} // namespace codes_zkw_range_sum_d59
