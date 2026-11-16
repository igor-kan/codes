#include "interface.hpp"
#include <algorithm>
#include <functional>

namespace codes_bridges_articulation_lowlink {
CutReport find_bridges_and_articulations(std::size_t n, const std::vector<UndirectedEdge>& edges) {
    CutReport rep;
    if (n == 0) return rep;
    std::vector<std::vector<std::pair<std::size_t, std::size_t>>> adj(n);
    for (std::size_t eid = 0; eid < edges.size(); ++eid) {
        const auto& e = edges[eid];
        if (e.u >= n || e.v >= n) return rep;
        adj[e.u].push_back({e.v, eid});
        adj[e.v].push_back({e.u, eid});
    }
    std::vector<int> tin(n, -1), low(n, -1);
    std::vector<bool> is_art(n, false);
    int timer = 0;
    std::function<void(std::size_t, std::size_t)> dfs = [&](std::size_t u, std::size_t peid) {
        tin[u] = low[u] = timer++;
        int children = 0;
        for (auto [to, eid] : adj[u]) {
            if (eid == peid) continue;
            if (tin[to] != -1) {
                low[u] = std::min(low[u], tin[to]);
            } else {
                ++children;
                dfs(to, eid);
                low[u] = std::min(low[u], low[to]);
                if (low[to] > tin[u]) {
                    rep.bridge_edge_ids.push_back(eid);
                }
                if (peid != edges.size() && low[to] >= tin[u]) {
                    is_art[u] = true;
                }
            }
        }
        if (peid == edges.size() && children > 1) {
            is_art[u] = true;
        }
    };
    for (std::size_t v = 0; v < n; ++v) {
        if (tin[v] == -1) dfs(v, edges.size());
    }
    for (std::size_t v = 0; v < n; ++v) {
        if (is_art[v]) rep.articulation_vertices.push_back(v);
    }
    std::sort(rep.bridge_edge_ids.begin(), rep.bridge_edge_ids.end());
    return rep;
}
} // namespace codes_bridges_articulation_lowlink
