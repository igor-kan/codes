// Single-source shortest paths in a DAG (CLRS 24.2).
#include <algorithm>
#include <cassert>
#include <iostream>
#include <limits>
#include <queue>
#include <vector>

int main() {
    const int n = 6;
    const long INF = std::numeric_limits<long>::max() / 4;
    std::vector<std::vector<std::pair<int, int>>> adj(n);
    auto add = [&](int u, int v, int w) { adj[u].push_back({v, w}); };
    add(0, 1, 5); add(0, 2, 3); add(1, 2, 2); add(1, 3, 6);
    add(2, 3, 7); add(2, 4, 4); add(2, 5, 2); add(3, 4, -1);
    add(3, 5, 1); add(4, 5, -2);

    std::vector<int> indegree(n, 0);
    for (int u = 0; u < n; ++u) for (auto &e : adj[u]) indegree[e.first]++;
    std::queue<int> queue;
    for (int i = 0; i < n; ++i) if (indegree[i] == 0) queue.push(i);
    std::vector<int> order;
    while (!queue.empty()) {
        int u = queue.front(); queue.pop();
        order.push_back(u);
        for (auto &e : adj[u]) if (--indegree[e.first] == 0) queue.push(e.first);
    }

    std::vector<long> dist(n, INF);
    dist[0] = 0;
    for (int u : order)
        for (auto &e : adj[u])
            if (dist[u] != INF) dist[e.first] = std::min(dist[e.first], dist[u] + e.second);
    assert(dist[3] == 10 && dist[4] == 7 && dist[5] == 5);
    std::cout << "dag shortest path ok\n";
    return 0;
}
