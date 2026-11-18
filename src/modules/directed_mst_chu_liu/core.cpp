#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_directed_mst_chu_liu {

std::int64_t edmonds_directed_mst(int n, int root, std::vector<DirEdge> edges) {
    std::int64_t res = 0;
    const std::int64_t INF = std::numeric_limits<std::int64_t>::max() / 4;
    while (true) {
        std::vector<std::int64_t> in(n, INF);
        std::vector<int> pre(n, -1);
        for (const auto& e : edges) {
            if (e.u != e.v && e.w < in[e.v]) {
                in[e.v] = e.w;
                pre[e.v] = e.u;
            }
        }
        for (int i = 0; i < n; ++i) {
            if (i != root && in[i] == INF) return -1;
        }
        int tn = 0;
        std::vector<int> id(n, -1), vis(n, -1);
        in[root] = 0;
        for (int i = 0; i < n; ++i) {
            res += in[i];
            int v = i;
            while (vis[v] != i && id[v] == -1 && v != root) {
                vis[v] = i;
                v = pre[v];
            }
            if (v != root && id[v] == -1) {
                for (int u = pre[v]; u != v; u = pre[u]) id[u] = tn;
                id[v] = tn++;
            }
        }
        if (tn == 0) break;
        for (int i = 0; i < n; ++i) if (id[i] == -1) id[i] = tn++;
        for (auto& e : edges) {
            int v = e.v;
            e.u = id[e.u];
            e.v = id[e.v];
            if (e.u != e.v) e.w -= in[v];
        }
        n = tn;
        root = id[root];
    }
    return res;
}

} // namespace codes_directed_mst_chu_liu
