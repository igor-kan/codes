#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_euler_tour_subtree_d59 {

std::vector<long long> all_subtree_sums(int n, int root, const std::vector<long long>& weights, const std::vector<std::pair<int, int>>& edges) {
    std::vector<std::vector<int>> adj(n);
    for (auto [u, v] : edges) { adj[u].push_back(v); adj[v].push_back(u); }
    std::vector<int> tin(n, 0), tout(n, 0);
    std::vector<long long> flat(n + 1, 0);
    int timer = 0;
    auto dfs = [&](auto& self, int u, int p) -> void {
        tin[u] = ++timer;
        flat[timer] = weights[u];
        for (int v : adj[u]) if (v != p) self(self, v, u);
        tout[u] = timer;
    };
    dfs(dfs, root, -1);
    std::vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; ++i) pref[i] = pref[i - 1] + flat[i];
    std::vector<long long> out(n);
    for (int i = 0; i < n; ++i) out[i] = pref[tout[i]] - pref[tin[i] - 1];
    return out;
}

} // namespace codes_euler_tour_subtree_d59
