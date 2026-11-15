#include "interface.hpp"
#include <limits>

namespace codes_floyd_warshall_apsp {
ApspResult solve_apsp(std::size_t n, const std::vector<double>& adj_weights) {
    const double INF = std::numeric_limits<double>::infinity();
    ApspResult res;
    res.n = n;
    res.dist = adj_weights;
    res.next_hop.assign(n * n, -1);
    for (std::size_t i = 0; i < n; ++i) {
        for (std::size_t j = 0; j < n; ++j) {
            if (res.dist[i * n + j] < INF) res.next_hop[i * n + j] = static_cast<int>(j);
        }
    }
    for (std::size_t k = 0; k < n; ++k) {
        for (std::size_t i = 0; i < n; ++i) {
            const double dik = res.dist[i * n + k];
            if (dik == INF) continue;
            for (std::size_t j = 0; j < n; ++j) {
                const double dkj = res.dist[k * n + j];
                if (dkj == INF) continue;
                if (dik + dkj < res.dist[i * n + j]) {
                    res.dist[i * n + j] = dik + dkj;
                    res.next_hop[i * n + j] = res.next_hop[i * n + k];
                }
            }
        }
    }
    for (std::size_t i = 0; i < n; ++i) {
        if (res.dist[i * n + i] < -1e-12) { res.has_negative_cycle = true; break; }
    }
    return res;
}

std::vector<int> reconstruct_path(const ApspResult& res, std::size_t u, std::size_t v) {
    std::vector<int> path;
    if (res.has_negative_cycle || u >= res.n || v >= res.n) return path;
    if (res.next_hop[u * res.n + v] == -1) return path;
    std::size_t cur = u;
    path.push_back(static_cast<int>(cur));
    for (std::size_t steps = 0; steps < res.n && cur != v; ++steps) {
        int nxt = res.next_hop[cur * res.n + v];
        if (nxt < 0) return {};
        cur = static_cast<std::size_t>(nxt);
        path.push_back(nxt);
    }
    return (cur == v) ? path : std::vector<int>{};
}
} // namespace codes_floyd_warshall_apsp
