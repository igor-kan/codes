#include <iostream>
#include <vector>
#include <stack>
#include <cassert>

class KosarajuSCC {
public:
    int n;
    std::vector<std::vector<int>> adj, rev_adj;

    explicit KosarajuSCC(int nodes) : n(nodes), adj(nodes), rev_adj(nodes) {}

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        rev_adj[v].push_back(u);
    }

    void dfs1(int u, std::vector<bool>& visited, std::vector<int>& order) {
        visited[u] = true;
        for (int v : adj[u]) {
            if (!visited[v]) dfs1(v, visited, order);
        }
        order.push_back(u);
    }

    void dfs2(int u, std::vector<bool>& visited, std::vector<int>& comp) {
        visited[u] = true;
        comp.push_back(u);
        for (int v : rev_adj[u]) {
            if (!visited[v]) dfs2(v, visited, comp);
        }
    }

    std::vector<std::vector<int>> getSCCs() {
        std::vector<bool> visited(n, false);
        std::vector<int> order;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) dfs1(i, visited, order);
        }

        std::fill(visited.begin(), visited.end(), false);
        std::vector<std::vector<int>> sccs;

        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            if (!visited[u]) {
                std::vector<int> comp;
                dfs2(u, visited, comp);
                sccs.push_back(comp);
            }
        }
        return sccs;
    }
};

int main() {
    KosarajuSCC g(5);
    g.addEdge(1, 0);
    g.addEdge(0, 2);
    g.addEdge(2, 1);
    g.addEdge(0, 3);
    g.addEdge(3, 4);

    auto sccs = g.getSCCs();
    assert(sccs.size() == 3);
    std::cout << "[C++ SCC] Kosaraju found 3 components." << std::endl;
    return 0;
}
