/**
 * Topological Sort (Kahn's Algorithm) in C++.
 */

#include <iostream>
#include <vector>
#include <queue>
#include <cassert>

std::vector<int> kahns_topological_sort(int n, const std::vector<std::pair<int, int>>& edges) {
    std::vector<std::vector<int>> adj(n);
    std::vector<int> in_degree(n, 0);

    for (const auto& edge : edges) {
        adj[edge.first].push_back(edge.second);
        in_degree[edge.second]++;
    }

    std::queue<int> q;
    for (int i = 0; i < n; ++i) {
        if (in_degree[i] == 0) {
            q.push(i);
        }
    }

    std::vector<int> order;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);

        for (int v : adj[u]) {
            if (--in_degree[v] == 0) {
                q.push(v);
            }
        }
    }

    if ((int)order.size() != n) {
        return {}; // Cycle detected
    }
    return order;
}

int main() {
    std::vector<std::pair<int, int>> edges = {
        {5, 2}, {5, 0}, {4, 0}, {4, 1}, {2, 3}, {3, 1}
    };
    int n = 6;
    auto order = kahns_topological_sort(n, edges);
    assert(order.size() == 6);

    std::vector<int> pos(n);
    for (int i = 0; i < n; ++i) {
        pos[order[i]] = i;
    }
    for (const auto& edge : edges) {
        assert(pos[edge.first] < pos[edge.second]);
    }

    std::cout << "[C++ TopoSort] Topological order verified." << std::endl;
    return 0;
}
