#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_min_cost_max_flow_d58 {

std::pair<long long, long long> min_cost_max_flow(int n, int s, int t, const std::vector<CostArc>& arcs) {
    struct E { int to, rev; long long cap, cost; };
    std::vector<std::vector<E>> g(n);
    for (const auto& a : arcs) {
        g[a.u].push_back({a.v, static_cast<int>(g[a.v].size()), a.cap, a.cost});
        g[a.v].push_back({a.u, static_cast<int>(g[a.u].size()) - 1, 0, -a.cost});
    }
    const long long INF = 1000000000000000LL;
    long long flow = 0, cost = 0;
    while (true) {
        std::vector<long long> dist(n, INF);
        std::vector<int> pv(n, -1), pe(n, -1);
        std::vector<bool> inq(n, false);
        std::deque<int> q = {s};
        dist[s] = 0; inq[s] = true;
        while (!q.empty()) {
            int u = q.front(); q.pop_front(); inq[u] = false;
            for (int i = 0; i < static_cast<int>(g[u].size()); ++i) {
                const auto& e = g[u][i];
                if (e.cap > 0 && dist[u] + e.cost < dist[e.to]) {
                    dist[e.to] = dist[u] + e.cost;
                    pv[e.to] = u; pe[e.to] = i;
                    if (!inq[e.to]) { q.push_back(e.to); inq[e.to] = true; }
                }
            }
        }
        if (dist[t] >= INF) break;
        long long add = INF;
        for (int v = t; v != s; v = pv[v]) add = std::min(add, g[pv[v]][pe[v]].cap);
        for (int v = t; v != s; v = pv[v]) {
            auto& fwd = g[pv[v]][pe[v]];
            fwd.cap -= add;
            g[v][fwd.rev].cap += add;
        }
        flow += add;
        cost += add * dist[t];
    }
    return {flow, cost};
}

} // namespace codes_min_cost_max_flow_d58
