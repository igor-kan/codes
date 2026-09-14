/**
 * Bipartite check via BFS two-coloring.
 */

#include <vector>
#include <queue>
#include <cassert>
#include <iostream>

bool isBipartite(const std::vector<std::vector<int>>& adj) {
    int n = static_cast<int>(adj.size());
    std::vector<int> color(n, -1);
    for (int s = 0; s < n; ++s) {
        if (color[s] != -1) continue;
        std::queue<int> q;
        q.push(s);
        color[s] = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    q.push(v);
                } else if (color[v] == color[u]) {
                    return false;
                }
            }
        }
    }
    return true;
}

int main() {
    std::vector<std::vector<int>> bipartite = {{1, 3}, {0, 2}, {1, 3}, {0, 2}};
    assert(isBipartite(bipartite));

    std::vector<std::vector<int>> odd = {{1, 2}, {0, 2}, {0, 1}}; // triangle
    assert(!isBipartite(odd));

    std::vector<std::vector<int>> disconnected = {{1}, {0}, {}, {4}, {3}};
    assert(isBipartite(disconnected));

    std::cout << "[C++ BipartiteCheck] BFS two-coloring verified." << std::endl;
    return 0;
}
