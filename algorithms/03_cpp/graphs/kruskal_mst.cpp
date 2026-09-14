// Kruskal's MST with a disjoint-set union structure.
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

struct Edge {
    int u;
    int v;
    int weight;
};

struct DSU {
    std::vector<int> parent;
    explicit DSU(int n) : parent(n) { std::iota(parent.begin(), parent.end(), 0); }
    int find(int x) { return parent[x] == x ? x : parent[x] = find(parent[x]); }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        parent[b] = a;
        return true;
    }
};

int kruskal(int n, std::vector<Edge> edges) {
    std::sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) { return a.weight < b.weight; });
    DSU dsu(n);
    int total = 0;
    for (const auto &e : edges)
        if (dsu.unite(e.u, e.v)) total += e.weight;
    return total;
}

int main() {
    int total = kruskal(4, {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}});
    std::cout << "mst=" << total << '\n';
    return total == 19 ? 0 : 1;
}
