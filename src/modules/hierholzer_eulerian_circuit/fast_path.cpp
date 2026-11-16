#include "interface.hpp"
#include <algorithm>

namespace codes_hierholzer_eulerian_circuit {
EulerResult find_directed_euler_fast(std::size_t n, const std::vector<DirectedEdge>& edges) {
    EulerResult out{};
    if (validate_euler_input(n, edges) != Status::Ok) return out;
    if (edges.empty()) {
        out.valid = true;
        out.vertices = {0};
        return out;
    }
    const std::size_t m = edges.size();
    std::vector<std::size_t> in_deg(n, 0), offset(n + 1, 0);
    for (const auto& e : edges) {
        ++offset[e.u + 1];
        ++in_deg[e.v];
    }
    std::size_t start = n, plus1 = 0, minus1 = 0;
    for (std::size_t v = 0; v < n; ++v) {
        std::size_t od = offset[v + 1];
        if (od > in_deg[v]) {
            if (od - in_deg[v] != 1) return out;
            ++plus1;
            start = v;
        } else if (in_deg[v] > od) {
            if (in_deg[v] - od != 1) return out;
            ++minus1;
        } else if (od > 0 && start == n) {
            start = v;
        }
        offset[v + 1] += offset[v];
    }
    if (!((plus1 == 0 && minus1 == 0) || (plus1 == 1 && minus1 == 1)) || start == n) return out;
    std::vector<std::size_t> cursor = offset;
    std::vector<std::pair<std::size_t, std::size_t>> flat_adj(m);
    for (std::size_t eid = 0; eid < m; ++eid) {
        flat_adj[cursor[edges[eid].u]++] = {edges[eid].v, eid};
    }
    std::vector<std::size_t> head(offset.begin(), offset.begin() + static_cast<std::ptrdiff_t>(n));
    std::vector<std::pair<std::size_t, std::size_t>> stk;
    stk.reserve(m + 1);
    stk.push_back({start, m});
    out.vertices.reserve(m + 1);
    out.edge_ids.reserve(m);
    while (!stk.empty()) {
        std::size_t u = stk.back().first;
        if (head[u] < offset[u + 1]) {
            auto [v, eid] = flat_adj[head[u]++];
            stk.push_back({v, eid});
        } else {
            out.vertices.push_back(u);
            if (stk.back().second != m) out.edge_ids.push_back(stk.back().second);
            stk.pop_back();
        }
    }
    if (out.edge_ids.size() != m) {
        out.vertices.clear();
        out.edge_ids.clear();
        return out;
    }
    std::reverse(out.vertices.begin(), out.vertices.end());
    std::reverse(out.edge_ids.begin(), out.edge_ids.end());
    out.valid = true;
    return out;
}
} // namespace codes_hierholzer_eulerian_circuit
