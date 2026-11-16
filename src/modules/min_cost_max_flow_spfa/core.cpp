#include "interface.hpp"
#include <algorithm>
#include <limits>
#include <queue>

namespace codes_min_cost_max_flow_spfa {
namespace {
struct ResEdge { std::size_t to, rev; int64_t cap, cost; int64_t orig_idx; };
}
FlowSolution solve_mcmf_spfa(std::size_t n, std::size_t src, std::size_t dst, const std::vector<FlowArc>& arcs) {
    FlowSolution sol{};
    if (validate_flow_network(n, src, dst, arcs) != Status::Ok) return sol;
    std::vector<std::vector<ResEdge>> g(n);
    for (std::size_t i = 0; i < arcs.size(); ++i) {
        const auto& a = arcs[i];
        std::size_t r_u = g[a.to].size();
        std::size_t r_v = g[a.from].size();
        g[a.from].push_back({a.to, r_u, a.cap, a.cost, static_cast<int64_t>(i)});
        g[a.to].push_back({a.from, r_v, 0, -a.cost, -1});
    }
    const int64_t INF = std::numeric_limits<int64_t>::max() / 4;
    std::vector<int64_t> dist(n), pv(n), pe(n);
    std::vector<bool> in_q(n);
    while (true) {
        std::fill(dist.begin(), dist.end(), INF);
        std::fill(in_q.begin(), in_q.end(), false);
        std::queue<std::size_t> q;
        dist[src] = 0;
        q.push(src);
        in_q[src] = true;
        while (!q.empty()) {
            std::size_t u = q.front();
            q.pop();
            in_q[u] = false;
            for (std::size_t i = 0; i < g[u].size(); ++i) {
                const auto& e = g[u][i];
                if (e.cap > 0 && dist[u] + e.cost < dist[e.to]) {
                    dist[e.to] = dist[u] + e.cost;
                    pv[e.to] = static_cast<int64_t>(u);
                    pe[e.to] = static_cast<int64_t>(i);
                    if (!in_q[e.to]) {
                        q.push(e.to);
                        in_q[e.to] = true;
                    }
                }
            }
        }
        if (dist[dst] >= INF) break;
        int64_t push = INF;
        for (std::size_t v = dst; v != src; v = static_cast<std::size_t>(pv[v])) {
            push = std::min(push, g[pv[v]][pe[v]].cap);
        }
        sol.total_flow += push;
        sol.total_cost += push * dist[dst];
        for (std::size_t v = dst; v != src; v = static_cast<std::size_t>(pv[v])) {
            auto& e = g[pv[v]][pe[v]];
            e.cap -= push;
            g[v][e.rev].cap += push;
        }
    }
    sol.arc_flows.assign(arcs.size(), 0);
    for (std::size_t u = 0; u < n; ++u) {
        for (const auto& e : g[u]) {
            if (e.orig_idx >= 0) {
                sol.arc_flows[static_cast<std::size_t>(e.orig_idx)] = arcs[static_cast<std::size_t>(e.orig_idx)].cap - e.cap;
            }
        }
    }
    return sol;
}
} // namespace codes_min_cost_max_flow_spfa
