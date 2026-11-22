#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_edmonds_karp_flow_d57 {

long long edmonds_karp_maxflow(int n, int s, int t, const std::vector<FlowEdgeSpec>& edges) {
    if (n <= 1 || s < 0 || s >= n || t < 0 || t >= n || s == t) throw std::invalid_argument("invalid endpoints");
    struct ResEdge { int to; int rev; long long cap; };
    std::vector<std::vector<ResEdge>> g(n);
    for (const auto& e : edges) {
        if (e.cap < 0) throw std::invalid_argument("negative capacity");
        int r1 = static_cast<int>(g[e.v].size());
        int r2 = static_cast<int>(g[e.u].size());
        g[e.u].push_back({e.v, r1, e.cap});
        g[e.v].push_back({e.u, r2, 0});
    }
    long long flow = 0;
    while (true) {
        std::vector<int> pv(n, -1), pe(n, -1);
        std::vector<int> q = {s};
        pv[s] = s;
        for (std::size_t qi = 0; qi < q.size() && pv[t] == -1; ++qi) {
            int u = q[qi];
            for (int ei = 0; ei < static_cast<int>(g[u].size()); ++ei) {
                const auto& e = g[u][ei];
                if (pv[e.to] == -1 && e.cap > 0) {
                    pv[e.to] = u;
                    pe[e.to] = ei;
                    q.push_back(e.to);
                }
            }
        }
        if (pv[t] == -1) break;
        long long add = std::numeric_limits<long long>::max();
        for (int v = t; v != s; v = pv[v]) {
            add = std::min(add, g[pv[v]][pe[v]].cap);
        }
        for (int v = t; v != s; v = pv[v]) {
            auto& fwd = g[pv[v]][pe[v]];
            fwd.cap -= add;
            g[v][fwd.rev].cap += add;
        }
        flow += add;
    }
    return flow;
}

} // namespace codes_edmonds_karp_flow_d57
