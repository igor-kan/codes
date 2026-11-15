#include "interface.hpp"
#include <deque>
#include <limits>

namespace codes_bellman_ford_spfa {
SsspResult solve_spfa_slf(std::size_t n, const std::vector<std::vector<Edge>>& adj, std::size_t src) {
    const double INF = std::numeric_limits<double>::infinity();
    SsspResult res;
    res.dist.assign(n, INF);
    res.parent.assign(n, -1);
    if (src >= n) return res;
    std::vector<bool> in_q(n, false);
    std::vector<std::size_t> cnt(n, 0);
    std::deque<std::size_t> dq;
    res.dist[src] = 0.0; dq.push_back(src); in_q[src] = true;
    while (!dq.empty()) {
        std::size_t u = dq.front(); dq.pop_front(); in_q[u] = false;
        for (const auto& e : adj[u]) {
            if (res.dist[u] + e.w < res.dist[e.to]) {
                res.dist[e.to] = res.dist[u] + e.w;
                res.parent[e.to] = static_cast<int>(u);
                if (!in_q[e.to]) {
                    if (++cnt[e.to] >= n) { res.negative_cycle = true; return res; }
                    if (!dq.empty() && res.dist[e.to] < res.dist[dq.front()]) dq.push_front(e.to);
                    else dq.push_back(e.to);
                    in_q[e.to] = true;
                }
            }
        }
    }
    return res;
}
} // namespace codes_bellman_ford_spfa
