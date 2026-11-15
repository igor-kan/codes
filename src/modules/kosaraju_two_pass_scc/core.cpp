#include "interface.hpp"

namespace codes_kosaraju_two_pass_scc {
static void dfs1(std::size_t u, const std::vector<std::vector<std::size_t>>& adj, std::vector<bool>& vis, std::vector<std::size_t>& order) {
    vis[u] = true;
    for (std::size_t v : adj[u]) {
        if (!vis[v]) dfs1(v, adj, vis, order);
    }
    order.push_back(u);
}

static void dfs2(std::size_t u, std::size_t cid, const std::vector<std::vector<std::size_t>>& radj, std::vector<std::size_t>& comp, std::vector<bool>& vis) {
    vis[u] = true;
    comp[u] = cid;
    for (std::size_t v : radj[u]) {
        if (!vis[v]) dfs2(v, cid, radj, comp, vis);
    }
}

SccResult find_scc(std::size_t n, const std::vector<std::vector<std::size_t>>& adj) {
    SccResult res;
    res.comp_id.assign(n, 0);
    std::vector<std::vector<std::size_t>> radj(n);
    for (std::size_t u = 0; u < n; ++u) {
        for (std::size_t v : adj[u]) radj[v].push_back(u);
    }
    std::vector<bool> vis(n, false);
    std::vector<std::size_t> order;
    order.reserve(n);
    for (std::size_t i = 0; i < n; ++i) {
        if (!vis[i]) dfs1(i, adj, vis, order);
    }
    std::fill(vis.begin(), vis.end(), false);
    for (std::size_t idx = order.size(); idx > 0; --idx) {
        std::size_t u = order[idx - 1];
        if (!vis[u]) {
            dfs2(u, res.num_components++, radj, res.comp_id, vis);
        }
    }
    return res;
}
} // namespace codes_kosaraju_two_pass_scc
