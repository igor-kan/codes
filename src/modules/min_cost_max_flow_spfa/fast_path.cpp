#include "interface.hpp"
#include <algorithm>
#include <limits>
#include <queue>

namespace codes_min_cost_max_flow_spfa {
FlowSolution solve_mcmf_potentials(std::size_t n, std::size_t src, std::size_t dst, const std::vector<FlowArc>& arcs) {
    FlowSolution sol{};
    if (validate_flow_network(n, src, dst, arcs) != Status::Ok) return sol;
    struct Edge { std::size_t to, rev; int64_t cap, cost, orig; };
    std::vector<std::vector<Edge>> g(n);
    for (std::size_t i = 0; i < arcs.size(); ++i) {
        const auto& a = arcs[i];
        std::size_t ru = g[a.to].size(), rv = g[a.from].size();
        g[a.from].push_back({a.to, ru, a.cap, a.cost, static_cast<int64_t>(i)});
        g[a.to].push_back({a.from, rv, 0, -a.cost, -1});
    }
    const int64_t INF = std::numeric_limits<int64_t>::max() / 4;
    std::vector<int64_t> pot(n, 0), dist(n), pv(n), pe(n);
    using P = std::pair<int64_t, std::size_t>;
    while (true) {
        std::fill(dist.begin(), dist.end(), INF);
        dist[src] = 0;
        std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
        pq.push({0, src});
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d != dist[u]) continue;
            for (std::size_t i = 0; i < g[u].size(); ++i) {
                const auto& e = g[u][i];
                int64_t nd = d + e.cost + pot[u] - pot[e.to];
                if (e.cap > 0 && nd < dist[e.to]) {
                    dist[e.to] = nd;
                    pv[e.to] = static_cast<int64_t>(u);
                    pe[e.to] = static_cast<int64_t>(i);
                    pq.push({nd, e.to});
                }
            }
        }
        if (dist[dst] >= INF) break;
        for (std::size_t v = 0; v < n; ++v) {
            if (dist[v] < INF) pot[v] += dist[v];
        }
        int64_t push = INF;
        for (std::size_t v = dst; v != src; v = static_cast<std::size_t>(pv[v])) {
            push = std::min(push, g[pv[v]][pe[v]].cap);
        }
        sol.total_flow += push;
        sol.total_cost += push * pot[dst];
        for (std::size_t v = dst; v != src; v = static_cast<std::size_t>(pv[v])) {
            auto& e = g[pv[v]][pe[v]];
            e.cap -= push;
            g[v][e.rev].cap += push;
        }
    }
    sol.arc_flows.assign(arcs.size(), 0);
    for (std::size_t u = 0; u < n; ++u) {
        for (const auto& e : g[u]) {
            if (e.orig >= 0) sol.arc_flows[static_cast<std::size_t>(e.orig)] = arcs[static_cast<std::size_t>(e.orig)].cap - e.cap;
        }
    }
    return sol;
}
} // namespace codes_min_cost_max_flow_spfa
