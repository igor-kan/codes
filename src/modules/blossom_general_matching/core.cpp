#include "interface.hpp"
#include <algorithm>
#include <queue>

namespace codes_blossom_general_matching {

MatchingResult edmonds_blossom_matching(int n, const std::vector<std::pair<int, int>>& edges) {
    validate_matching_input(n, edges);
    std::vector<std::vector<int>> adj(static_cast<std::size_t>(n));
    for (const auto& e : edges) {
        adj[static_cast<std::size_t>(e.first)].push_back(e.second);
        adj[static_cast<std::size_t>(e.second)].push_back(e.first);
    }
    std::vector<int> match(static_cast<std::size_t>(n), -1);
    std::vector<int> p(static_cast<std::size_t>(n), -1);
    std::vector<int> base(static_cast<std::size_t>(n));
    std::vector<bool> used(static_cast<std::size_t>(n));
    std::vector<bool> blossom(static_cast<std::size_t>(n));

    auto lca = [&](int a, int b) -> int {
        std::vector<bool> vis(static_cast<std::size_t>(n), false);
        while (true) {
            a = base[static_cast<std::size_t>(a)];
            vis[static_cast<std::size_t>(a)] = true;
            if (match[static_cast<std::size_t>(a)] == -1) break;
            a = p[static_cast<std::size_t>(match[static_cast<std::size_t>(a)])];
        }
        while (true) {
            b = base[static_cast<std::size_t>(b)];
            if (vis[static_cast<std::size_t>(b)]) return b;
            b = p[static_cast<std::size_t>(match[static_cast<std::size_t>(b)])];
        }
    };

    auto mark_path = [&](int v, int b, int children) {
        while (base[static_cast<std::size_t>(v)] != b) {
            blossom[static_cast<std::size_t>(base[static_cast<std::size_t>(v)])] = true;
            blossom[static_cast<std::size_t>(base[static_cast<std::size_t>(match[static_cast<std::size_t>(v)])])] = true;
            p[static_cast<std::size_t>(v)] = children;
            children = match[static_cast<std::size_t>(v)];
            v = p[static_cast<std::size_t>(match[static_cast<std::size_t>(v)])];
        }
    };

    auto find_path = [&](int root) -> int {
        std::fill(used.begin(), used.end(), false);
        std::fill(p.begin(), p.end(), -1);
        for (int i = 0; i < n; ++i) base[static_cast<std::size_t>(i)] = i;
        std::queue<int> q;
        used[static_cast<std::size_t>(root)] = true;
        q.push(root);
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int to : adj[static_cast<std::size_t>(v)]) {
                if (base[static_cast<std::size_t>(v)] == base[static_cast<std::size_t>(to)] ||
                    match[static_cast<std::size_t>(v)] == to) {
                    continue;
                }
                if (to == root || (match[static_cast<std::size_t>(to)] != -1 &&
                                   p[static_cast<std::size_t>(match[static_cast<std::size_t>(to)])] != -1)) {
                    int cur_base = lca(v, to);
                    std::fill(blossom.begin(), blossom.end(), false);
                    mark_path(v, cur_base, to);
                    mark_path(to, cur_base, v);
                    for (int i = 0; i < n; ++i) {
                        if (blossom[static_cast<std::size_t>(base[static_cast<std::size_t>(i)])]) {
                            base[static_cast<std::size_t>(i)] = cur_base;
                            if (!used[static_cast<std::size_t>(i)]) {
                                used[static_cast<std::size_t>(i)] = true;
                                q.push(i);
                            }
                        }
                    }
                } else if (p[static_cast<std::size_t>(to)] == -1) {
                    p[static_cast<std::size_t>(to)] = v;
                    if (match[static_cast<std::size_t>(to)] == -1) return to;
                    int nxt = match[static_cast<std::size_t>(to)];
                    used[static_cast<std::size_t>(nxt)] = true;
                    q.push(nxt);
                }
            }
        }
        return -1;
    };

    int pairs = fast_greedy_warm_match(n, adj, match);
    for (int i = 0; i < n; ++i) {
        if (match[static_cast<std::size_t>(i)] == -1) {
            int v = find_path(i);
            if (v != -1) ++pairs;
            while (v != -1) {
                int pv = p[static_cast<std::size_t>(v)];
                int ppv = match[static_cast<std::size_t>(pv)];
                match[static_cast<std::size_t>(v)] = pv;
                match[static_cast<std::size_t>(pv)] = v;
                v = ppv;
            }
        }
    }
    return {pairs, match};
}

} // namespace codes_blossom_general_matching
