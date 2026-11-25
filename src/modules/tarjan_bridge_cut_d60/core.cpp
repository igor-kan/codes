#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_tarjan_bridge_cut_d60 {

CutResult find_bridges_and_cuts(int n, const std::vector<GraphEdge>& edges) {
    std::vector<std::vector<std::pair<int, int>>> adj(n);
    for (int i = 0; i < static_cast<int>(edges.size()); ++i) {
        adj[edges[i].u].push_back({edges[i].v, i});
        adj[edges[i].v].push_back({edges[i].u, i});
    }
    std::vector<int> tin(n, -1), low(n, -1);
    std::vector<bool> is_cut(n, false);
    CutResult res;
    int timer = 0;
    auto dfs = [&](auto& self, int u, int pe) -> void {
        tin[u] = low[u] = timer++;
        int children = 0;
        for (auto [v, eid] : adj[u]) {
            if (eid == pe) continue;
            if (tin[v] != -1) {
                low[u] = std::min(low[u], tin[v]);
            } else {
                self(self, v, eid);
                low[u] = std::min(low[u], low[v]);
                if (low[v] > tin[u]) res.bridges.push_back({std::min(u, v), std::max(u, v)});
                if (low[v] >= tin[u] && pe != -1) is_cut[u] = true;
                ++children;
            }
        }
        if (pe == -1 && children > 1) is_cut[u] = true;
    };
    for (int i = 0; i < n; ++i) {
        if (tin[i] == -1) dfs(dfs, i, -1);
    }
    for (int i = 0; i < n; ++i) {
        if (is_cut[i]) res.cut_vertices.push_back(i);
    }
    return res;
}

} // namespace codes_tarjan_bridge_cut_d60
