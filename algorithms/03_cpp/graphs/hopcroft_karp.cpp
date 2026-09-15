// Hopcroft-Karp bipartite matching.
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

const int INF = 1 << 30;

bool bfs(const std::vector<std::vector<int>> &adj, std::vector<int> &pair_u,
         std::vector<int> &pair_v, std::vector<int> &dist) {
    std::queue<int> queue;
    for (std::size_t u = 0; u < adj.size(); ++u) {
        if (pair_u[u] == -1) { dist[u] = 0; queue.push(static_cast<int>(u)); }
        else dist[u] = INF;
    }
    bool found = false;
    while (!queue.empty()) {
        int u = queue.front();
        queue.pop();
        for (int v : adj[u]) {
            int w = pair_v[v];
            if (w == -1) found = true;
            else if (dist[w] == INF) { dist[w] = dist[u] + 1; queue.push(w); }
        }
    }
    return found;
}

bool dfs(int u, const std::vector<std::vector<int>> &adj, std::vector<int> &pair_u,
         std::vector<int> &pair_v, std::vector<int> &dist) {
    for (int v : adj[u]) {
        int w = pair_v[v];
        if (w == -1 || (dist[w] == dist[u] + 1 && dfs(w, adj, pair_u, pair_v, dist))) {
            pair_u[u] = v;
            pair_v[v] = u;
            return true;
        }
    }
    dist[u] = INF;
    return false;
}

int hopcroft_karp(const std::vector<std::vector<int>> &adj, int right_size) {
    std::vector<int> pair_u(adj.size(), -1), pair_v(right_size, -1), dist(adj.size());
    int matching = 0;
    while (bfs(adj, pair_u, pair_v, dist))
        for (std::size_t u = 0; u < adj.size(); ++u)
            if (pair_u[u] == -1 && dfs(static_cast<int>(u), adj, pair_u, pair_v, dist)) ++matching;
    return matching;
}

int main() {
    std::vector<std::vector<int>> adj{{0, 1}, {0}, {1, 2}, {2}};
    assert(hopcroft_karp(adj, 3) == 3);
    std::cout << "hopcroft-karp ok\n";
    return 0;
}
