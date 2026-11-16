#include "interface.hpp"
#include <algorithm>
#include <stdexcept>

namespace codes_sparse_table_rmq_o1 {
SparseTable build_sparse_table(const std::vector<int64_t>& arr) {
    SparseTable t;
    t.n = arr.size();
    if (t.n == 0) return t;
    t.lg2.assign(t.n + 1, 0);
    for (std::size_t i = 2; i <= t.n; ++i) t.lg2[i] = t.lg2[i / 2] + 1;
    std::size_t K = t.lg2[t.n] + 1;
    t.st.assign(K, std::vector<int64_t>(t.n, 0));
    t.st[0] = arr;
    for (std::size_t k = 1; k < K; ++k) {
        std::size_t step = std::size_t(1) << (k - 1);
        std::size_t span = std::size_t(1) << k;
        for (std::size_t i = 0; i + span <= t.n; ++i) {
            t.st[k][i] = std::min(t.st[k - 1][i], t.st[k - 1][i + step]);
        }
    }
    return t;
}

int64_t query_rmq_o1(const SparseTable& tab, std::size_t l, std::size_t r) {
    if (validate_query(tab, l, r) != Status::Ok) throw std::out_of_range("invalid RMQ bounds");
    std::size_t k = tab.lg2[r - l + 1];
    return std::min(tab.st[k][l], tab.st[k][r + 1 - (std::size_t(1) << k)]);
}
} // namespace codes_sparse_table_rmq_o1
