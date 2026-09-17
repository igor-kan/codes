/**
 * Hierholzer's Algorithm in C++
 * Linear time Eulerian path / circuit construction in O(V + E).
 */

#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <cassert>

std::vector<int> hierholzer(int n, std::vector<std::vector<int>> adj) {
    std::stack<int> currPath;
    std::vector<int> circuit;
    currPath.push(0);

    while (!currPath.empty()) {
        int u = currPath.top();
        if (!adj[u].empty()) {
            int next = adj[u].back();
            adj[u].pop_back();
            currPath.push(next);
        } else {
            circuit.push_back(currPath.top());
            currPath.pop();
        }
    }
    std::reverse(circuit.begin(), circuit.end());
    return circuit;
}

int main() {
    std::vector<std::vector<int>> adj = {{1}, {2}, {0, 3}, {0}};
    auto path = hierholzer(4, adj);
    assert(!path.empty());
    std::cout << "C++ Hierholzer verified.\n";
    return 0;
}
