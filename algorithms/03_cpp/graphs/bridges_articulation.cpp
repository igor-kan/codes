/**
 * Tarjan's algorithm for bridges and articulation points in an undirected graph.
 */

#include <vector>
#include <algorithm>
#include <set>
#include <cassert>
#include <iostream>

class Tarjan {
    int n, timer;
    std::vector<std::vector<int>> adj;
    std::vector<int> tin, low;
    std::vector<bool> visited;
    std::vector<std::pair<int, int>> bridges;
    std::set<int> articulation;

    void dfs(int v, int p) {
        visited[v] = true;
        tin[v] = low[v] = timer++;
        int children = 0;
        for (int to : adj[v]) {
            if (to == p) continue;
            if (visited[to]) {
                low[v] = std::min(low[v], tin[to]);
            } else {
                dfs(to, v);
                low[v] = std::min(low[v], low[to]);
                if (low[to] > tin[v]) bridges.push_back({v, to});
                if (low[to] >= tin[v] && p != -1) articulation.insert(v);
                ++children;
            }
        }
        if (p == -1 && children > 1) articulation.insert(v);
    }

public:
    Tarjan(int n, const std::vector<std::vector<int>>& g) : n(n), timer(0), adj(g) {
        tin.assign(n, -1);
        low.assign(n, -1);
        visited.assign(n, false);
        for (int i = 0; i < n; ++i)
            if (!visited[i]) dfs(i, -1);
    }

    std::vector<std::pair<int, int>> bridgesSorted() const {
        auto b = bridges;
        for (auto& e : b) if (e.first > e.second) std::swap(e.first, e.second);
        std::sort(b.begin(), b.end());
        return b;
    }

    std::vector<int> articulationSorted() const {
        return std::vector<int>(articulation.begin(), articulation.end());
    }
};

int main() {
    std::vector<std::vector<int>> g(5);
    auto addEdge = [&](int u, int v) { g[u].push_back(v); g[v].push_back(u); };
    addEdge(0, 1);
    addEdge(1, 2);
    addEdge(2, 0);
    addEdge(0, 3);
    addEdge(3, 4);

    Tarjan tarjan(5, g);
    auto bridges = tarjan.bridgesSorted();
    assert((bridges == std::vector<std::pair<int, int>>{{0, 3}, {3, 4}}));
    assert((tarjan.articulationSorted() == std::vector<int>{0, 3}));

    std::cout << "[C++ BridgesArticulation] Tarjan bridges and articulation points verified." << std::endl;
    return 0;
}
