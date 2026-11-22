#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_centroid_tree_dist_d57 {

TreeExtent compute_tree_extent(int n, const std::vector<std::pair<int, int>>& edges) {
    if (n <= 0 || static_cast<int>(edges.size()) != n - 1) throw std::invalid_argument("valid tree required");
    if (n == 1) return {0, 0};
    std::vector<std::vector<int>> adj(n);
    for (auto [u, v] : edges) {
        if (u < 0 || u >= n || v < 0 || v >= n) throw std::out_of_range("bad vertex");
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    auto bfs = [&](int start) -> std::pair<int, int> {
        std::vector<int> d(n, -1);
        std::vector<int> q = {start};
        d[start] = 0;
        int far = start;
        for (std::size_t i = 0; i < q.size(); ++i) {
            int u = q[i];
            if (d[u] > d[far]) far = u;
            for (int v : adj[u]) {
                if (d[v] == -1) { d[v] = d[u] + 1; q.push_back(v); }
            }
        }
        if (static_cast<int>(q.size()) != n) throw std::invalid_argument("disconnected tree");
        return {far, d[far]};
    };
    int end_a = bfs(0).first;
    int diam = bfs(end_a).second;
    return {diam, (diam + 1) / 2};
}

} // namespace codes_centroid_tree_dist_d57
