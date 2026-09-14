/**
 * Dinic's maximum flow algorithm.
 */

#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <cassert>
#include <iostream>

class Dinic {
    struct Edge {
        int to, rev;
        long long cap;
    };
    int n;
    std::vector<std::vector<Edge>> g;
    std::vector<int> level, it;

    bool bfs(int s, int t) {
        std::fill(level.begin(), level.end(), -1);
        std::queue<int> q;
        q.push(s);
        level[s] = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (const auto& e : g[u]) {
                if (e.cap > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int u, int t, long long f) {
        if (u == t) return f;
        for (int& i = it[u]; i < static_cast<int>(g[u].size()); ++i) {
            Edge& e = g[u][i];
            if (e.cap > 0 && level[e.to] == level[u] + 1) {
                long long d = dfs(e.to, t, std::min(f, e.cap));
                if (d > 0) {
                    e.cap -= d;
                    g[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }

public:
    explicit Dinic(int n) : n(n), g(n), level(n), it(n) {}

    void addEdge(int u, int v, long long cap) {
        g[u].push_back({v, static_cast<int>(g[v].size()), cap});
        g[v].push_back({u, static_cast<int>(g[u].size()) - 1, 0});
    }

    long long maxFlow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            std::fill(it.begin(), it.end(), 0);
            while (long long f = dfs(s, t, LLONG_MAX)) flow += f;
        }
        return flow;
    }
};

int main() {
    Dinic dinic(4);
    dinic.addEdge(0, 1, 16);
    dinic.addEdge(0, 2, 13);
    dinic.addEdge(1, 2, 10);
    dinic.addEdge(1, 3, 12);
    dinic.addEdge(2, 1, 4);
    dinic.addEdge(2, 3, 14);
    assert(dinic.maxFlow(0, 3) == 26);

    Dinic simple(3);
    simple.addEdge(0, 1, 5);
    simple.addEdge(1, 2, 5);
    assert(simple.maxFlow(0, 2) == 5);

    std::cout << "[C++ MaxFlowDinic] Dinic max flow verified." << std::endl;
    return 0;
}
