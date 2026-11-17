#include "interface.hpp"
#include <thread>

namespace codes_centroid_decomposition_tree {
std::vector<int> parallel_multi_query(
    int n,
    const std::vector<std::pair<int, int>>& edges,
    const std::vector<int>& actives,
    const std::vector<int>& queries
) {
    CentroidOracle oracle(n, edges);
    for (int a : actives) oracle.activate(a);
    std::vector<int> out(queries.size(), -1);
    std::size_t mid = queries.size() / 2;
    auto run = [&](std::size_t lo, std::size_t hi) {
        for (std::size_t i = lo; i < hi; ++i) out[i] = oracle.nearest_active_dist(queries[i]);
    };
    std::thread t1(run, 0, mid);
    std::thread t2(run, mid, queries.size());
    t1.join();
    t2.join();
    return out;
}
} // namespace codes_centroid_decomposition_tree
