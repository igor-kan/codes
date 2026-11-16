#include "interface.hpp"
#include <algorithm>

namespace codes_sparse_table_rmq_o1 {
Status verify_table_invariants(const SparseTable& tab, const std::vector<int64_t>& arr) {
    if (tab.n != arr.size()) return Status::InvariantViolation;
    for (std::size_t l = 0; l < arr.size(); ++l) {
        int64_t cur = arr[l];
        for (std::size_t r = l; r < arr.size(); ++r) {
            cur = std::min(cur, arr[r]);
            if (query_rmq_o1(tab, l, r) != cur) return Status::InvariantViolation;
        }
    }
    return Status::Ok;
}
} // namespace codes_sparse_table_rmq_o1
