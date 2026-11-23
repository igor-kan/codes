#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_heavy_light_lca_d58 {

BinaryLiftLca::BinaryLiftLca(int n, int root, const std::vector<std::pair<int, int>>& edges)
    : n_(n), lg_(1), depth_(n, 0) {
    while ((1 << lg_) <= n) ++lg_;
    up_.assign(lg_, std::vector<int>(n, root));
    std::vector<std::vector<int>> adj(n);
    for (auto [u, v] : edges) { adj[u].push_back(v); adj[v].push_back(u); }
    std::vector<bool> vis(n, false);
    std::vector<int> q = {root};
    vis[root] = true;
    up_[0][root] = root;
    for (std::size_t qi = 0; qi < q.size(); ++qi) {
        int u = q[qi];
        for (int v : adj[u]) {
            if (!vis[v]) {
                vis[v] = true;
                depth_[v] = depth_[u] + 1;
                up_[0][v] = u;
                q.push_back(v);
            }
        }
    }
    for (int k = 1; k < lg_; ++k) {
        for (int v = 0; v < n; ++v) up_[k][v] = up_[k - 1][up_[k - 1][v]];
    }
}

int BinaryLiftLca::lca(int u, int v) const {
    if (depth_[u] < depth_[v]) std::swap(u, v);
    int diff = depth_[u] - depth_[v];
    for (int k = 0; k < lg_; ++k) if (diff & (1 << k)) u = up_[k][u];
    if (u == v) return u;
    for (int k = lg_ - 1; k >= 0; --k) {
        if (up_[k][u] != up_[k][v]) { u = up_[k][u]; v = up_[k][v]; }
    }
    return up_[0][u];
}

int BinaryLiftLca::dist(int u, int v) const {
    int c = lca(u, v);
    return depth_[u] + depth_[v] - 2 * depth_[c];
}

} // namespace codes_heavy_light_lca_d58
