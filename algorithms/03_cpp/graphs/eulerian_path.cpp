/**
 * Hierholzer's algorithm for an Eulerian path/circuit in a directed graph.
 */

#include <vector>
#include <stack>
#include <algorithm>
#include <cassert>
#include <iostream>

// Returns a vertex sequence covering every edge exactly once, or empty if impossible.
std::vector<int> eulerianPath(std::vector<std::vector<int>> adj) {
    int n = static_cast<int>(adj.size());
    std::vector<int> in(n, 0), out(n, 0);
    for (int u = 0; u < n; ++u) {
        out[u] += static_cast<int>(adj[u].size());
        for (int v : adj[u]) in[v]++;
    }

    int start = -1, cntStart = 0, cntEnd = 0;
    for (int i = 0; i < n; ++i) {
        if (out[i] - in[i] == 1) { start = i; ++cntStart; }
        else if (in[i] - out[i] == 1) ++cntEnd;
        else if (in[i] != out[i]) return {};
    }
    if (cntStart > 1 || cntEnd > 1 || cntStart != cntEnd) return {};
    if (start == -1) {
        for (int i = 0; i < n; ++i)
            if (out[i] > 0) { start = i; break; }
        if (start == -1) start = 0;
    }

    std::vector<int> path;
    std::stack<int> st;
    st.push(start);
    while (!st.empty()) {
        int u = st.top();
        if (!adj[u].empty()) {
            int v = adj[u].back();
            adj[u].pop_back();
            st.push(v);
        } else {
            path.push_back(u);
            st.pop();
        }
    }
    std::reverse(path.begin(), path.end());
    return path;
}

int main() {
    std::vector<std::vector<int>> g(4);
    g[0] = {1};
    g[1] = {2};
    g[2] = {3};
    auto path = eulerianPath(g);
    assert((path == std::vector<int>{0, 1, 2, 3}));

    std::vector<std::vector<int>> circuit(3);
    circuit[0] = {1};
    circuit[1] = {2};
    circuit[2] = {0};
    auto c = eulerianPath(circuit);
    assert(c.size() == 4 && c.front() == c.back());

    // Two independent components each with a single edge: no single Eulerian path.
    std::vector<std::vector<int>> impossible(4);
    impossible[0] = {1};
    impossible[2] = {3};
    assert(eulerianPath(impossible).empty());

    std::cout << "[C++ EulerianPath] Hierholzer's algorithm verified." << std::endl;
    return 0;
}
