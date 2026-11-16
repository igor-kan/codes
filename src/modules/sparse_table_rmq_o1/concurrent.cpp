#include "interface.hpp"
#include <algorithm>
#include <thread>

namespace codes_sparse_table_rmq_o1 {
std::vector<int64_t> batch_query_rmq(const SparseTable& tab, const std::vector<std::pair<std::size_t, std::size_t>>& queries) {
    std::vector<int64_t> out(queries.size(), 0);
    if (queries.empty()) return out;
    std::size_t nt = std::min<std::size_t>(4, queries.size());
    std::vector<std::thread> pool;
    for (std::size_t t = 0; t < nt; ++t) {
        pool.emplace_back([&, t]() {
            for (std::size_t i = t; i < queries.size(); i += nt) {
                out[i] = query_rmq_o1(tab, queries[i].first, queries[i].second);
            }
        });
    }
    for (auto& th : pool) th.join();
    return out;
}
} // namespace codes_sparse_table_rmq_o1
