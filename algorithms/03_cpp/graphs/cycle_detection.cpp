/**
 * Cycle detection for directed (DFS states) and undirected (parent) graphs.
 */

#include <vector>
#include <stack>
#include <cassert>
#include <iostream>

bool dfsDirected(int u, const std::vector<std::vector<int>>& adj, std::vector<int>& state) {
    state[u] = 1; // visiting
    for (int v : adj[u]) {
        if (state[v] == 1) return true;
        if (state[v] == 0 && dfsDirected(v, adj, state)) return true;
    }
    state[u] = 2; // done
    return false;
}

bool hasCycleDirected(const std::vector<std::vector<int>>& adj) {
    int n = static_cast<int>(adj.size());
    std::vector<int> state(n, 0);
    for (int s = 0; s < n; ++s)
        if (state[s] == 0 && dfsDirected(s, adj, state)) return true;
    return false;
}

bool hasCycleUndirected(const std::vector<std::vector<int>>& adj) {
    int n = static_cast<int>(adj.size());
    std::vector<bool> visited(n, false);
    for (int s = 0; s < n; ++s) {
        if (visited[s]) continue;
        std::stack<std::pair<int, int>> st;
        st.push({s, -1});
        visited[s] = true;
        while (!st.empty()) {
            auto [u, p] = st.top();
            st.pop();
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    st.push({v, u});
                } else if (v != p) {
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    std::vector<std::vector<int>> directedCycle = {{1}, {2}, {0}};
    assert(hasCycleDirected(directedCycle));
    std::vector<std::vector<int>> directedAcyclic = {{1}, {2}, {}};
    assert(!hasCycleDirected(directedAcyclic));

    std::vector<std::vector<int>> undirectedCycle = {{1, 2}, {0, 2}, {0, 1}};
    assert(hasCycleUndirected(undirectedCycle));
    std::vector<std::vector<int>> tree = {{1, 2}, {0}, {0}};
    assert(!hasCycleUndirected(tree));

    std::cout << "[C++ CycleDetection] Directed and undirected cycle detection verified." << std::endl;
    return 0;
}
