#include "interface.hpp"
namespace codes_topological_kahn_dag {
std::vector<std::vector<std::size_t>> kahn_level_waves(std::size_t n, const std::vector<std::vector<std::size_t>>& adj) {
    auto indeg = compute_in_degrees(n, adj);
    std::vector<std::vector<std::size_t>> waves;
    std::vector<std::size_t> cur;
    for (std::size_t i = 0; i < n; ++i) if (indeg[i] == 0) cur.push_back(i);
    while (!cur.empty()) {
        waves.push_back(cur);
        std::vector<std::size_t> nxt;
        for (std::size_t u : cur) for (std::size_t v : adj[u]) if (--indeg[v] == 0) nxt.push_back(v);
        cur = std::move(nxt);
    }
    return waves;
}
} // namespace codes_topological_kahn_dag
