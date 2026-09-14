/**
 * Kahn's algorithm for topological sort with cycle detection.
 */

#include <vector>
#include <queue>
#include <cassert>
#include <iostream>

// Returns a valid topological order, or an empty vector if the graph has a cycle.
std::vector<int> kahnTopoSort(int n, const std::vector<std::pair<int, int>>& edges) {
    std::vector<std::vector<int>> adj(n);
    std::vector<int> indeg(n, 0);
    for (const auto& [u, v] : edges) {
        adj[u].push_back(v);
        indeg[v]++;
    }

    std::queue<int> q;
    for (int i = 0; i < n; ++i)
        if (indeg[i] == 0) q.push(i);

    std::vector<int> order;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);
        for (int v : adj[u])
            if (--indeg[v] == 0) q.push(v);
    }
    if (static_cast<int>(order.size()) != n) return {}; // cycle detected
    return order;
}

int main() {
    std::vector<std::pair<int, int>> edges = {{5, 2}, {5, 0}, {4, 0}, {4, 1}, {2, 3}, {3, 1}};
    auto order = kahnTopoSort(6, edges);
    assert(order.size() == 6);
    std::vector<int> pos(6);
    for (int i = 0; i < 6; ++i) pos[order[i]] = i;
    for (const auto& [u, v] : edges) assert(pos[u] < pos[v]);

    std::vector<std::pair<int, int>> cyclic = {{0, 1}, {1, 2}, {2, 0}};
    assert(kahnTopoSort(3, cyclic).empty());

    std::cout << "[C++ KahnTopoSort] Topological order and cycle detection verified." << std::endl;
    return 0;
}
