#include "interface.hpp"
#include <thread>

namespace codes_link_cut_tree_splay {
std::vector<std::int64_t> parallel_forest_path_sums(
    int n,
    const std::vector<std::pair<int, int>>& edges,
    const std::vector<std::int64_t>& weights,
    const std::vector<std::pair<int, int>>& queries
) {
    std::vector<std::int64_t> results(queries.size(), 0);
    auto worker = [&](std::size_t lo, std::size_t hi) {
        LinkCutTree lct(n);
        for (int i = 0; i < n; ++i) lct.set_value(i, weights[static_cast<std::size_t>(i)]);
        for (const auto& e : edges) lct.link(e.first, e.second);
        for (std::size_t qi = lo; qi < hi; ++qi) {
            results[qi] = lct.query_path_sum(queries[qi].first, queries[qi].second);
        }
    };
    std::size_t mid = queries.size() / 2;
    std::thread t1(worker, 0, mid);
    std::thread t2(worker, mid, queries.size());
    t1.join();
    t2.join();
    return results;
}
} // namespace codes_link_cut_tree_splay
