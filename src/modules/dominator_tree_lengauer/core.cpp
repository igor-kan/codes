#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_dominator_tree_lengauer {

std::vector<int> compute_immediate_dominators(int n, int root, const std::vector<std::pair<int, int>>& edges) {
    std::vector<std::vector<int>> adj(n), radj(n);
    for (auto [u, v] : edges) {
        adj[u].push_back(v);
        radj[v].push_back(u);
    }
    std::vector<int> order, vis(n, 0);
    auto dfs = [&](auto& self, int u) -> void {
        vis[u] = 1;
        order.push_back(u);
        for (int w : adj[u]) if (!vis[w]) self(self, w);
    };
    dfs(dfs, root);
    std::vector<int> rpo_pos(n, -1);
    for (int i = 0; i < static_cast<int>(order.size()); ++i) rpo_pos[order[i]] = i;

    std::vector<int> idom(n, -1);
    idom[root] = root;
    auto intersect = [&](int b1, int b2) {
        while (b1 != b2) {
            while (rpo_pos[b1] > rpo_pos[b2]) b1 = idom[b1];
            while (rpo_pos[b2] > rpo_pos[b1]) b2 = idom[b2];
        }
        return b1;
    };
    bool changed = true;
    while (changed) {
        changed = false;
        for (int idx = 1; idx < static_cast<int>(order.size()); ++idx) {
            int u = order[idx];
            int new_idom = -1;
            for (int p : radj[u]) {
                if (idom[p] != -1) {
                    new_idom = (new_idom == -1) ? p : intersect(p, new_idom);
                }
            }
            if (new_idom != -1 && idom[u] != new_idom) {
                idom[u] = new_idom;
                changed = true;
            }
        }
    }
    return idom;
}

bool dominates(const std::vector<int>& idom, int u, int v) {
    int cur = v;
    while (cur != -1) {
        if (cur == u) return true;
        if (idom[cur] == cur) break;
        cur = idom[cur];
    }
    return false;
}

} // namespace codes_dominator_tree_lengauer
