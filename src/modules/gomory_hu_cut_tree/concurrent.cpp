#include "interface.hpp"
#include <thread>

namespace codes_gomory_hu_cut_tree {
std::vector<std::int64_t> parallel_cut_queries(
    int n,
    const std::vector<UndirectedEdge>& edges,
    const std::vector<std::pair<int, int>>& pairs
) {
    auto tree = build_gomory_hu_tree(n, edges);
    std::vector<std::int64_t> out(pairs.size(), 0);
    std::size_t mid = pairs.size() / 2;
    auto worker = [&](std::size_t lo, std::size_t hi) {
        for (std::size_t i = lo; i < hi; ++i) {
            out[i] = query_pair_min_cut(n, tree, pairs[i].first, pairs[i].second);
        }
    };
    std::thread t1(worker, 0, mid);
    std::thread t2(worker, mid, pairs.size());
    t1.join();
    t2.join();
    return out;
}
} // namespace codes_gomory_hu_cut_tree
