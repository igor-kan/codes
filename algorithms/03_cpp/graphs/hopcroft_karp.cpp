/**
 * Hopcroft-Karp Algorithm in C++
 * Maximum cardinality bipartite matching in O(E sqrt(V)).
 */

#include <iostream>
#include <vector>
#include <queue>
#include <cassert>

class HopcroftKarp {
    int nU, nV;
    std::vector<std::vector<int>> adj;
    std::vector<int> pairU, pairV, dist;

public:
    HopcroftKarp(int u, int v) : nU(u), nV(v), adj(u + 1), pairU(u + 1, 0), pairV(v + 1, 0), dist(u + 1, 0) {}

    void addEdge(int u, int v) { adj[u].push_back(v); }

    int maxMatching() {
        int matching = 0;
        while (bfs()) {
            for (int u = 1; u <= nU; u++) {
                if (pairU[u] == 0 && dfs(u)) matching++;
            }
        }
        return matching;
    }

private:
    bool bfs() {
        std::queue<int> q;
        for (int u = 1; u <= nU; u++) {
            if (pairU[u] == 0) { dist[u] = 0; q.push(u); }
            else dist[u] = 1e9;
        }
        dist[0] = 1e9;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            if (dist[u] < dist[0]) {
                for (int v : adj[u]) {
                    if (dist[pairV[v]] == 1e9) {
                        dist[pairV[v]] = dist[u] + 1;
                        q.push(pairV[v]);
                    }
                }
            }
        }
        return dist[0] != 1e9;
    }

    bool dfs(int u) {
        if (u != 0) {
            for (int v : adj[u]) {
                if (dist[pairV[v]] == dist[u] + 1 && dfs(pairV[v])) {
                    pairV[v] = u;
                    pairU[u] = v;
                    return true;
                }
            }
            dist[u] = 1e9;
            return false;
        }
        return true;
    }
};

int main() {
    HopcroftKarp hk(4, 4);
    hk.addEdge(1, 2);
    hk.addEdge(1, 3);
    hk.addEdge(2, 1);
    hk.addEdge(3, 2);
    hk.addEdge(4, 2);
    hk.addEdge(4, 4);
    assert(hk.maxMatching() == 4);
    std::cout << "C++ Hopcroft-Karp verified.\n";
    return 0;
}
