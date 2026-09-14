// Bellman-Ford with negative edge support and cycle detection.
#include <iostream>
#include <limits>
#include <optional>
#include <vector>

struct Edge {
    int from;
    int to;
    int weight;
};

std::optional<std::vector<long long>> bellman_ford(int n, const std::vector<Edge> &edges, int src) {
    const long long inf = std::numeric_limits<long long>::max() / 4;
    std::vector<long long> dist(n, inf);
    dist[src] = 0;
    for (int iter = 0; iter < n - 1; ++iter)
        for (const auto &e : edges)
            if (dist[e.from] != inf && dist[e.from] + e.weight < dist[e.to])
                dist[e.to] = dist[e.from] + e.weight;
    for (const auto &e : edges)
        if (dist[e.from] != inf && dist[e.from] + e.weight < dist[e.to])
            return std::nullopt;
    return dist;
}

int main() {
    std::vector<Edge> edges{{0, 1, 4}, {0, 2, 5}, {1, 2, -3}, {2, 3, 2}};
    auto dist = bellman_ford(4, edges, 0);
    if (!dist) return 1;
    for (long long d : *dist) std::cout << d << ' ';
    std::cout << '\n';
    return 0;
}
