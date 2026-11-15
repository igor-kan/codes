#include "interface.hpp"
#include <limits>
#include <queue>
#include <utility>

namespace codes_johnson_apsp_reweight {
static std::vector<double> dijkstra_from(std::size_t n, const std::vector<std::vector<WEdge>>& rw, std::size_t src) {
    const double INF = std::numeric_limits<double>::infinity();
    std::vector<double> d(n, INF);
    using P = std::pair<double, std::size_t>;
    std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
    d[src] = 0.0;
    pq.push({0.0, src});
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du > d[u] + 1e-12) continue;
        for (const auto& e : rw[u]) {
            if (du + e.w < d[e.to]) {
                d[e.to] = du + e.w;
                pq.push({d[e.to], e.to});
            }
        }
    }
    return d;
}

JohnsonOutput solve_johnson(std::size_t n, const std::vector<std::vector<WEdge>>& adj) {
    const double INF = std::numeric_limits<double>::infinity();
    JohnsonOutput out;
    out.potentials.assign(n, 0.0);
    for (std::size_t it = 0; it < n; ++it) {
        bool changed = false;
        for (std::size_t u = 0; u < n; ++u) {
            for (const auto& e : adj[u]) {
                if (out.potentials[u] + e.w < out.potentials[e.to]) {
                    out.potentials[e.to] = out.potentials[u] + e.w;
                    changed = true;
                }
            }
        }
        if (it == n - 1 && changed) {
            // Check 1 more pass strictly
            for (std::size_t u = 0; u < n; ++u) {
                for (const auto& e : adj[u]) {
                    if (out.potentials[u] + e.w + 1e-12 < out.potentials[e.to]) {
                        out.has_negative_cycle = true;
                        return out;
                    }
                }
            }
        }
        if (!changed) break;
    }
    std::vector<std::vector<WEdge>> rw(n);
    for (std::size_t u = 0; u < n; ++u) {
        for (const auto& e : adj[u]) {
            double nw = e.w + out.potentials[u] - out.potentials[e.to];
            rw[u].push_back({e.to, nw < 0.0 ? 0.0 : nw});
        }
    }
    out.dist.resize(n);
    for (std::size_t s = 0; s < n; ++s) {
        auto d = dijkstra_from(n, rw, s);
        for (std::size_t v = 0; v < n; ++v) {
            if (d[v] < INF) d[v] = d[v] - out.potentials[s] + out.potentials[v];
        }
        out.dist[s] = std::move(d);
    }
    return out;
}
} // namespace codes_johnson_apsp_reweight
