#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_sparse_table_rmq_d60 {

SparseTableRmq::SparseTableRmq(const std::vector<std::int64_t>& vals)
    : n_(static_cast<int>(vals.size())), lg_(n_ + 1, 0) {
    for (int i = 2; i <= n_; ++i) lg_[i] = lg_[i >> 1] + 1;
    int K = lg_[n_] + 1;
    st_.assign(K, std::vector<std::int64_t>(n_, 0));
    for (int i = 0; i < n_; ++i) st_[0][i] = vals[i];
    for (int k = 1; k < K; ++k) {
        int span = 1 << (k - 1);
        for (int i = 0; i + (1 << k) <= n_; ++i) {
            st_[k][i] = std::min(st_[k - 1][i], st_[k - 1][i + span]);
        }
    }
}
std::int64_t SparseTableRmq::query(int l, int r) const {
    int k = lg_[r - l + 1];
    return std::min(st_[k][l], st_[k][r - (1 << k) + 1]);
}

} // namespace codes_sparse_table_rmq_d60
