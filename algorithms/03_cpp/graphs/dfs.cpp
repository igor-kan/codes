#include <vector>
#include <stack>
#include <unordered_set>
#include <iostream>

std::vector<int> dfs(const std::vector<std::vector<int>>& g, int s) {
    std::unordered_set<int> visited;
    std::stack<int> stk;
    std::vector<int> order;
    stk.push(s);
    while (!stk.empty()) {
        int u = stk.top(); stk.pop();
        if (visited.insert(u).second) {
            order.push_back(u);
            const auto& neighbors = g[u];
            for (auto it = neighbors.rbegin(); it != neighbors.rend(); ++it)
                stk.push(*it);
        }
    }
    return order;
}

int main() {
    std::vector<std::vector<int>> g = {{1, 2}, {0, 3, 4}, {0, 5}, {1}, {1}, {2}};
    std::vector<int> order = dfs(g, 0);
    if (order.size() != 6 || order.front() != 0) {
        std::cerr << "[C++ DFS] FAILED: unexpected traversal size\n";
        return 1;
    }
    std::cout << "[C++ DFS] Iterative stack-based traversal verified: {";
    for (size_t i = 0; i < order.size(); ++i)
        std::cout << order[i] << (i + 1 < order.size() ? ", " : "}\n");
    return 0;
}
