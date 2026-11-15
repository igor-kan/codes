#include "interface.hpp"
#include <limits>
#include <queue>

namespace codes_bellman_ford_spfa {
SsspResult solve_bellman_ford(std::size_t n, const std::vector<std::vector<Edge>>& adj, std::size_t src) {
    const double INF = std::numeric_limits<double>::infinity();
    SsspResult res;
    res.dist.assign(n, INF);
    res.parent.assign(n, -1);
    if (src >= n) return res;
    res.dist[src] = 0.0;
    for (std::size_t it = 0; it + 1 < n; ++it) {
        bool changed = false;
        for (std::size_t u = 0; u < n; ++u) {
            if (res.dist[u] == INF) continue;
            for (const auto& e : adj[u]) {
                if (res.dist[u] + e.w < res.dist[e.to]) {
                    res.dist[e.to] = res.dist[u] + e.w;
                    res.parent[e.to] = static_cast<int>(u);
                    changed = true;
                }
            }
        }
        if (!changed) break;
    }
    for (std::size_t u = 0; u < n; ++u) {
        if (res.dist[u] == INF) continue;
        for (const auto& e : adj[u]) {
            if (res.dist[u] + e.w + 1e-12 < res.dist[e.to]) { res.negative_cycle = true; return res; }
        }
    }
    return res;
}

SsspResult solve_spfa(std::size_t n, const std::vector<std::vector<Edge>>& adj, std::size_t src) {
    const double INF = std::numeric_limits<double>::infinity();
    SsspResult res;
    res.dist.assign(n, INF);
    res.parent.assign(n, -1);
    if (src >= n) return res;
    std::vector<bool> in_q(n, false);
    std::vector<std::size_t> cnt(n, 0);
    std::queue<std::size_t> q;
    res.dist[src] = 0.0;
    q.push(src); in_q[src] = true;
    while (!q.empty()) {
        std::size_t u = q.front(); q.pop(); in_q[u] = false;
        for (const auto& e : adj[u]) {
            if (res.dist[u] + e.w < res.dist[e.to]) {
                res.dist[e.to] = res.dist[u] + e.w;
                res.parent[e.to] = static_cast<int>(u);
                if (!in_q[e.to]) {
                    q.push(e.to); in_q[e.to] = true;
                    if (++cnt[e.to] >= n) { res.negative_cycle = true; return res; }
                }
            }
        }
    }
    return res;
}
} // namespace codes_bellman_ford_spfa
