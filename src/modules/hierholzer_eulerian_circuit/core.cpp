#include "interface.hpp"
#include <algorithm>

namespace codes_hierholzer_eulerian_circuit {
EulerResult find_directed_euler(std::size_t n, const std::vector<DirectedEdge>& edges) {
    EulerResult out{};
    if (n == 0 || edges.empty()) {
        if (n > 0) {
            out.valid = true;
            out.vertices = {0};
        }
        return out;
    }
    std::vector<std::vector<std::pair<std::size_t, std::size_t>>> adj(n);
    std::vector<std::size_t> in_deg(n, 0), out_deg(n, 0);
    for (std::size_t eid = 0; eid < edges.size(); ++eid) {
        const auto& e = edges[eid];
        if (e.u >= n || e.v >= n) return out;
        adj[e.u].push_back({e.v, eid});
        ++out_deg[e.u];
        ++in_deg[e.v];
    }
    std::size_t start = n;
    std::size_t start_cand = 0, end_cand = 0;
    for (std::size_t v = 0; v < n; ++v) {
        if (out_deg[v] > in_deg[v]) {
            if (out_deg[v] - in_deg[v] != 1) return out;
            ++start_cand;
            start = v;
        } else if (in_deg[v] > out_deg[v]) {
            if (in_deg[v] - out_deg[v] != 1) return out;
            ++end_cand;
        } else if (out_deg[v] > 0 && start == n) {
            start = v;
        }
    }
    if (!((start_cand == 0 && end_cand == 0) || (start_cand == 1 && end_cand == 1)) || start == n) {
        return out;
    }
    std::vector<std::size_t> head(n, 0);
    std::vector<std::pair<std::size_t, std::size_t>> stk;
    stk.push_back({start, edges.size()});
    std::vector<std::size_t> verts, eids;
    while (!stk.empty()) {
        std::size_t u = stk.back().first;
        if (head[u] < adj[u].size()) {
            auto [v, eid] = adj[u][head[u]++];
            stk.push_back({v, eid});
        } else {
            verts.push_back(u);
            if (stk.back().second != edges.size()) {
                eids.push_back(stk.back().second);
            }
            stk.pop_back();
        }
    }
    if (eids.size() != edges.size()) return out;
    std::reverse(verts.begin(), verts.end());
    std::reverse(eids.begin(), eids.end());
    out.valid = true;
    out.vertices = std::move(verts);
    out.edge_ids = std::move(eids);
    return out;
}
} // namespace codes_hierholzer_eulerian_circuit
