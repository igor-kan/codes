#include "interface.hpp"
#include <algorithm>
#include <queue>

namespace codes_bridges_articulation_lowlink {
static std::size_t count_components(std::size_t n, const std::vector<UndirectedEdge>& edges, std::size_t skip_edge, std::size_t skip_vert) {
    std::vector<std::vector<std::size_t>> adj(n);
    for (std::size_t i = 0; i < edges.size(); ++i) {
        if (i == skip_edge) continue;
        if (edges[i].u == skip_vert || edges[i].v == skip_vert) continue;
        adj[edges[i].u].push_back(edges[i].v);
        adj[edges[i].v].push_back(edges[i].u);
    }
    std::vector<bool> vis(n, false);
    std::size_t comps = 0;
    std::queue<std::size_t> q;
    for (std::size_t v = 0; v < n; ++v) {
        if (v == skip_vert || vis[v]) continue;
        ++comps;
        vis[v] = true;
        q.push(v);
        while (!q.empty()) {
            std::size_t u = q.front();
            q.pop();
            for (std::size_t w : adj[u]) {
                if (!vis[w]) {
                    vis[w] = true;
                    q.push(w);
                }
            }
        }
    }
    return comps;
}

Status verify_cut_oracle(std::size_t n, const std::vector<UndirectedEdge>& edges, const CutReport& rep) {
    if (validate_graph(n, edges) != Status::Ok) return Status::InvalidInput;
    std::size_t base = count_components(n, edges, edges.size(), n);
    std::vector<bool> is_b(edges.size(), false);
    for (std::size_t eid : rep.bridge_edge_ids) is_b[eid] = true;
    for (std::size_t eid = 0; eid < edges.size(); ++eid) {
        std::size_t c = count_components(n, edges, eid, n);
        if ((c > base) != is_b[eid]) return Status::InvariantViolation;
    }
    std::vector<bool> is_a(n, false);
    for (std::size_t v : rep.articulation_vertices) is_a[v] = true;
    for (std::size_t v = 0; v < n; ++v) {
        bool has_edge = false;
        for (const auto& e : edges) {
            if (e.u == v || e.v == v) { has_edge = true; break; }
        }
        std::size_t c = count_components(n, edges, edges.size(), v);
        bool oracle_art = has_edge && (c > base);
        if (oracle_art != is_a[v]) return Status::InvariantViolation;
    }
    return Status::Ok;
}
} // namespace codes_bridges_articulation_lowlink
