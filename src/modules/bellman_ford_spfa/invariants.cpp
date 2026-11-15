#include "interface.hpp"
#include <limits>

namespace codes_bellman_ford_spfa {
Status verify_optimality(const std::vector<std::vector<Edge>>& adj, const SsspResult& res) {
    if (res.negative_cycle) return Status::Ok;
    const double INF = std::numeric_limits<double>::infinity();
    for (std::size_t u = 0; u < adj.size(); ++u) {
        if (res.dist[u] == INF) continue;
        for (const auto& e : adj[u]) {
            if (res.dist[u] + e.w + 1e-9 < res.dist[e.to]) return Status::InvariantViolation;
        }
    }
    return Status::Ok;
}
} // namespace codes_bellman_ford_spfa
