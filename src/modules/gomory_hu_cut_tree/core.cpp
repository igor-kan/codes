#include "interface.hpp"
#include <algorithm>
#include <limits>
#include <queue>

namespace codes_gomory_hu_cut_tree {

struct FlowEdge {
    int to;
    int rev;
    std::int64_t cap;
};

static std::int64_t dinic_min_cut(
    int n,
    const std::vector<UndirectedEdge>& base_edges,
    int s,
    int t,
    std::vector<bool>& s_side
) {
    std::vector<std::vector<FlowEdge>> g(static_cast<std::size_t>(n));
    for (const auto& e : base_edges) {
        int a = static_cast<int>(g[static_cast<std::size_t>(e.u)].size());
        int b = static_cast<int>(g[static_cast<std::size_t>(e.v)].size());
        g[static_cast<std::size_t>(e.u)].push_back({e.v, b, e.cap});
        g[static_cast<std::size_t>(e.v)].push_back({e.u, a, e.cap});
    }
    std::vector<int> level(static_cast<std::size_t>(n));
    std::vector<std::size_t> ptr(static_cast<std::size_t>(n));
    auto bfs = [&]() -> bool {
        std::fill(level.begin(), level.end(), -1);
        std::queue<int> q;
        level[static_cast<std::size_t>(s)] = 0;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (const auto& fe : g[static_cast<std::size_t>(u)]) {
                if (fe.cap > 0 && level[static_cast<std::size_t>(fe.to)] == -1) {
                    level[static_cast<std::size_t>(fe.to)] = level[static_cast<std::size_t>(u)] + 1;
                    q.push(fe.to);
                }
            }
        }
        return level[static_cast<std::size_t>(t)] != -1;
    };
    auto dfs = [&](auto& self, int u, std::int64_t pushed) -> std::int64_t {
        if (pushed == 0 || u == t) return pushed;
        for (std::size_t& cid = ptr[static_cast<std::size_t>(u)]; cid < g[static_cast<std::size_t>(u)].size(); ++cid) {
            auto& fe = g[static_cast<std::size_t>(u)][cid];
            if (fe.cap > 0 && level[static_cast<std::size_t>(fe.to)] == level[static_cast<std::size_t>(u)] + 1) {
                std::int64_t tr = self(self, fe.to, std::min(pushed, fe.cap));
                if (tr > 0) {
                    fe.cap -= tr;
                    g[static_cast<std::size_t>(fe.to)][static_cast<std::size_t>(fe.rev)].cap += tr;
                    return tr;
                }
            }
        }
        return 0;
    };
    std::int64_t flow = 0;
    const std::int64_t inf = std::numeric_limits<std::int64_t>::max() / 4;
    while (bfs()) {
        std::fill(ptr.begin(), ptr.end(), 0);
        while (std::int64_t pushed = dfs(dfs, s, inf)) flow += pushed;
    }
    s_side.assign(static_cast<std::size_t>(n), false);
    for (int i = 0; i < n; ++i) s_side[static_cast<std::size_t>(i)] = (level[static_cast<std::size_t>(i)] != -1);
    return flow;
}

std::vector<GhEdge> build_gomory_hu_tree(int n, const std::vector<UndirectedEdge>& edges) {
    validate_graph(n, edges);
    std::vector<int> p(static_cast<std::size_t>(n), 0);
    std::vector<GhEdge> tree;
    tree.reserve(static_cast<std::size_t>(n > 0 ? n - 1 : 0));
    std::vector<bool> s_side;
    for (int i = 1; i < n; ++i) {
        int parent = p[static_cast<std::size_t>(i)];
        std::int64_t cut = dinic_min_cut(n, edges, i, parent, s_side);
        tree.push_back({i, parent, cut});
        for (int j = i + 1; j < n; ++j) {
            if (s_side[static_cast<std::size_t>(j)] && p[static_cast<std::size_t>(j)] == parent) {
                p[static_cast<std::size_t>(j)] = i;
            }
        }
    }
    return tree;
}

std::int64_t query_pair_min_cut(int n, const std::vector<GhEdge>& tree, int s, int t) {
    if (s == t) return 0;
    std::vector<std::vector<std::pair<int, std::int64_t>>> adj(static_cast<std::size_t>(n));
    for (const auto& e : tree) {
        adj[static_cast<std::size_t>(e.u)].emplace_back(e.v, e.min_cut);
        adj[static_cast<std::size_t>(e.v)].emplace_back(e.u, e.min_cut);
    }
    std::int64_t ans = std::numeric_limits<std::int64_t>::max();
    auto dfs = [&](auto& self, int u, int par, std::int64_t cur_min) -> bool {
        if (u == t) { ans = cur_min; return true; }
        for (const auto& [v, w] : adj[static_cast<std::size_t>(u)]) {
            if (v != par && self(self, v, u, std::min(cur_min, w))) return true;
        }
        return false;
    };
    dfs(dfs, s, -1, ans);
    return ans;
}

} // namespace codes_gomory_hu_cut_tree
