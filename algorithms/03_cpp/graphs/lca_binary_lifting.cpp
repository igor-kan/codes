/**
 * Lowest Common Ancestor via binary lifting.
 */

#include <vector>
#include <stack>
#include <algorithm>
#include <cassert>
#include <iostream>

class LCA {
    int n, LOG;
    std::vector<std::vector<int>> up;
    std::vector<int> depth;

public:
    LCA(const std::vector<std::vector<int>>& adj, int root) : n(static_cast<int>(adj.size())) {
        LOG = 1;
        while ((1 << LOG) <= n) ++LOG;
        up.assign(LOG, std::vector<int>(n, -1));
        depth.assign(n, 0);

        std::vector<bool> visited(n, false);
        std::stack<int> st;
        st.push(root);
        visited[root] = true;
        up[0][root] = root;
        while (!st.empty()) {
            int u = st.top();
            st.pop();
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    up[0][v] = u;
                    depth[v] = depth[u] + 1;
                    st.push(v);
                }
            }
        }

        for (int j = 1; j < LOG; ++j)
            for (int i = 0; i < n; ++i)
                if (up[j - 1][i] != -1)
                    up[j][i] = up[j - 1][up[j - 1][i]];
    }

    int lca(int a, int b) {
        if (depth[a] < depth[b]) std::swap(a, b);
        int diff = depth[a] - depth[b];
        for (int j = 0; j < LOG; ++j)
            if (diff & (1 << j)) a = up[j][a];
        if (a == b) return a;
        for (int j = LOG - 1; j >= 0; --j)
            if (up[j][a] != up[j][b]) {
                a = up[j][a];
                b = up[j][b];
            }
        return up[0][a];
    }
};

int main() {
    std::vector<std::vector<int>> adj(7);
    auto addEdge = [&](int u, int v) { adj[u].push_back(v); adj[v].push_back(u); };
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 3);
    addEdge(1, 4);
    addEdge(2, 5);
    addEdge(2, 6);

    LCA lca(adj, 0);
    assert(lca.lca(3, 4) == 1);
    assert(lca.lca(3, 5) == 0);
    assert(lca.lca(5, 6) == 2);
    assert(lca.lca(1, 3) == 1);
    assert(lca.lca(6, 6) == 6);

    std::cout << "[C++ LCA] Binary lifting lowest common ancestor verified." << std::endl;
    return 0;
}
