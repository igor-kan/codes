#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <cassert>

struct Edge {
    int to;
    double weight;
};

using AdjList = std::vector<std::vector<Edge>>;

std::vector<double> dijkstra(int source, const AdjList& adj) {
    size_t n = adj.size();
    std::vector<double> dist(n, std::numeric_limits<double>::infinity());
    dist[source] = 0.0;

    using Pair = std::pair<double, int>; // (distance, vertex)
    std::priority_queue<Pair, std::vector<Pair>, std::greater<Pair>> pq;
    pq.emplace(0.0, source);

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;

        for (const auto& edge : adj[u]) {
            if (dist[u] + edge.weight < dist[edge.to]) {
                dist[edge.to] = dist[u] + edge.weight;
                pq.emplace(dist[edge.to], edge.to);
            }
        }
    }
    return dist;
}

int main() {
    AdjList adj(4);
    adj[0].push_back({1, 4.0});
    adj[0].push_back({2, 1.0});
    adj[2].push_back({1, 2.0});
    adj[1].push_back({3, 1.0});
    adj[2].push_back({3, 5.0});

    auto dist = dijkstra(0, adj);
    assert(dist[3] == 4.0);
    std::cout << "[C++ Dijkstra] Shortest path 0 -> 3: " << dist[3] << " verified." << std::endl;
    return 0;
}
