#include "interface.hpp"
#include <algorithm>
#include <vector>

namespace codes_sparse_table_rmq_o1 {
std::vector<int64_t> query_rmq_batch_single(const SparseTable& tab, const std::vector<std::pair<std::size_t, std::size_t>>& qs) {
    std::vector<int64_t> ans(qs.size());
    for (std::size_t i = 0; i < qs.size(); ++i) {
        ans[i] = query_rmq_o1(tab, qs[i].first, qs[i].second);
    }
    return ans;
}
} // namespace codes_sparse_table_rmq_o1
