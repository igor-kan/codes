/**
 * Disjoint Set Union (Union-Find) with path compression + union by size.
 */

#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

class DSU {
    std::vector<int> parent;
    std::vector<int> sz;
public:
    explicit DSU(int n) : parent(n), sz(n, 1) {
        for (int i = 0; i < n; ++i) parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (sz[a] < sz[b]) std::swap(a, b);
        parent[b] = a;
        sz[a] += sz[b];
        return true;
    }

    int size(int x) { return sz[find(x)]; }
};

int main() {
    DSU dsu(6);
    assert(dsu.unite(0, 1));
    assert(dsu.unite(1, 2));
    assert(!dsu.unite(0, 2));       // already connected
    assert(dsu.find(0) == dsu.find(2));
    assert(dsu.size(0) == 3);
    dsu.unite(3, 4);
    dsu.unite(4, 5);
    assert(dsu.size(3) == 3);
    dsu.unite(2, 5);
    assert(dsu.size(0) == 6);       // all merged into one component
    std::cout << "[C++ DSU] Union-find with path compression and size verified." << std::endl;
    return 0;
}
