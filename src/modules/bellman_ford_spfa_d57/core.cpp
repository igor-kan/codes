#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_bellman_ford_spfa_d57 {

std::pair<bool, std::vector<long long>> bellman_ford_solve(int n, int src, const std::vector<DirWeightedEdge>& edges) {
    if (n <= 0 || src < 0 || src >= n) throw std::invalid_argument("invalid graph dimensions");
    const long long INF = 1000000000000000LL;
    std::vector<long long> dist(n, INF);
    dist[src] = 0;
    for (int i = 0; i < n - 1; ++i) {
        bool changed = false;
        for (const auto& e : edges) {
            if (dist[e.u] < INF && dist[e.u] + e.w < dist[e.v]) {
                dist[e.v] = dist[e.u] + e.w;
                changed = true;
            }
        }
        if (!changed) break;
    }
    for (const auto& e : edges) {
        if (dist[e.u] < INF && dist[e.u] + e.w < dist[e.v]) {
            return {true, dist};
        }
    }
    return {false, dist};
}

} // namespace codes_bellman_ford_spfa_d57
