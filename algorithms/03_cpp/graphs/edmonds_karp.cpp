// Edmonds-Karp maximum flow.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

int edmonds_karp(std::vector<std::vector<int>> capacity, int source, int sink) {
    const int n = static_cast<int>(capacity.size());
    int flow = 0;
    while (true) {
        std::vector<int> parent(n, -1);
        parent[source] = source;
        std::queue<int> queue;
        queue.push(source);
        while (!queue.empty() && parent[sink] == -1) {
            int u = queue.front();
            queue.pop();
            for (int v = 0; v < n; ++v)
                if (parent[v] == -1 && capacity[u][v] > 0) {
                    parent[v] = u;
                    queue.push(v);
                }
        }
        if (parent[sink] == -1) break;
        int bottleneck = 1 << 30;
        for (int v = sink; v != source; v = parent[v]) bottleneck = std::min(bottleneck, capacity[parent[v]][v]);
        for (int v = sink; v != source; v = parent[v]) {
            capacity[parent[v]][v] -= bottleneck;
            capacity[v][parent[v]] += bottleneck;
        }
        flow += bottleneck;
    }
    return flow;
}

int main() {
    std::vector<std::vector<int>> capacity{
        {0, 16, 13, 0, 0, 0}, {0, 0, 10, 12, 0, 0}, {0, 4, 0, 0, 14, 0},
        {0, 0, 9, 0, 0, 20}, {0, 0, 0, 7, 0, 4}, {0, 0, 0, 0, 0, 0}};
    assert(edmonds_karp(capacity, 0, 5) == 23);
    std::cout << "edmonds-karp ok\n";
    return 0;
}
