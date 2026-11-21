#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_dijkstra_minheap_sp {

std::vector<long long> dijkstra_distances(int n, int src, const std::vector<std::vector<std::pair<int, long long>>>& adj) {
    if (n <= 0 || src < 0 || src >= n || static_cast<int>(adj.size()) != n) {
        throw std::invalid_argument("invalid graph dimensions");
    }
    const long long INF = std::numeric_limits<long long>::max() / 4;
    std::vector<long long> dist(n, INF);
    using Node = std::pair<long long, int>;
    std::priority_queue<Node, std::vector<Node>, std::greater<Node>> pq;
    dist[src] = 0;
    pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u]) continue;
        for (const auto& [v, w] : adj[u]) {
            if (w < 0) throw std::invalid_argument("negative edge weight disallowed");
            if (d + w < dist[v]) {
                dist[v] = d + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

} // namespace codes_dijkstra_minheap_sp
