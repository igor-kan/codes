#include "interface.hpp"
#include <algorithm>

namespace codes_bridges_articulation_lowlink {
CutReport find_bridges_iterative(std::size_t n, const std::vector<UndirectedEdge>& edges) {
    CutReport rep;
    if (validate_graph(n, edges) != Status::Ok) return rep;
    std::vector<std::size_t> offset(n + 1, 0);
    for (const auto& e : edges) {
        ++offset[e.u + 1];
        ++offset[e.v + 1];
    }
    for (std::size_t i = 0; i < n; ++i) offset[i + 1] += offset[i];
    std::vector<std::size_t> cursor = offset;
    std::vector<std::pair<std::size_t, std::size_t>> flat(2 * edges.size());
    for (std::size_t eid = 0; eid < edges.size(); ++eid) {
        flat[cursor[edges[eid].u]++] = {edges[eid].v, eid};
        flat[cursor[edges[eid].v]++] = {edges[eid].u, eid};
    }
    std::vector<int> tin(n, -1), low(n, -1), root_children(n, 0);
    std::vector<bool> is_art(n, false);
    struct Frame { std::size_t u, peid, idx, pvert; };
    std::vector<Frame> stk;
    int timer = 0;
    for (std::size_t root = 0; root < n; ++root) {
        if (tin[root] != -1) continue;
        tin[root] = low[root] = timer++;
        stk.push_back({root, edges.size(), offset[root], n});
        while (!stk.empty()) {
            Frame& f = stk.back();
            if (f.idx < offset[f.u + 1]) {
                auto [to, eid] = flat[f.idx++];
                if (eid == f.peid) continue;
                if (tin[to] != -1) {
                    low[f.u] = std::min(low[f.u], tin[to]);
                } else {
                    if (f.pvert == n) ++root_children[f.u];
                    tin[to] = low[to] = timer++;
                    stk.push_back({to, eid, offset[to], f.u});
                }
            } else {
                std::size_t child = f.u, parent = f.pvert, ceid = f.peid;
                stk.pop_back();
                if (parent != n) {
                    low[parent] = std::min(low[parent], low[child]);
                    if (low[child] > tin[parent]) rep.bridge_edge_ids.push_back(ceid);
                    if (parent != root && low[child] >= tin[parent]) is_art[parent] = true;
                }
            }
        }
        if (root_children[root] > 1) is_art[root] = true;
    }
    for (std::size_t v = 0; v < n; ++v) {
        if (is_art[v]) rep.articulation_vertices.push_back(v);
    }
    std::sort(rep.bridge_edge_ids.begin(), rep.bridge_edge_ids.end());
    return rep;
}
} // namespace codes_bridges_articulation_lowlink
