#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_dinic_scaling_maxflow {

ScalingDinic::ScalingDinic(int n) : n_(n), adj_(n), level_(n), ptr_(n) {}

void ScalingDinic::add_edge(int u, int v, std::int64_t cap) {
    FlowEdge fwd{v, static_cast<int>(adj_[v].size()), cap};
    FlowEdge bwd{u, static_cast<int>(adj_[u].size()), 0};
    adj_[u].push_back(fwd);
    adj_[v].push_back(bwd);
}

bool ScalingDinic::bfs(int s, int t, std::int64_t delta) {
    std::fill(level_.begin(), level_.end(), -1);
    level_[s] = 0;
    std::queue<int> q;
    q.push(s);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (const auto& e : adj_[u]) {
            if (e.cap >= delta && level_[e.to] < 0) {
                level_[e.to] = level_[u] + 1;
                q.push(e.to);
            }
        }
    }
    return level_[t] >= 0;
}

std::int64_t ScalingDinic::dfs(int u, int t, std::int64_t pushed, std::int64_t delta) {
    if (pushed == 0 || u == t) return pushed;
    for (std::size_t& cid = ptr_[u]; cid < adj_[u].size(); ++cid) {
        auto& e = adj_[u][cid];
        if (level_[e.to] != level_[u] + 1 || e.cap < delta) continue;
        std::int64_t tr = dfs(e.to, t, std::min(pushed, e.cap), delta);
        if (tr == 0) continue;
        e.cap -= tr;
        adj_[e.to][e.rev].cap += tr;
        return tr;
    }
    return 0;
}

std::int64_t ScalingDinic::max_flow(int s, int t) {
    std::int64_t max_c = 0;
    for (const auto& lst : adj_) for (const auto& e : lst) max_c = std::max(max_c, e.cap);
    std::int64_t delta = 1;
    while (delta <= max_c / 2) delta <<= 1;
    std::int64_t flow = 0;
    for (; delta > 0; delta >>= 1) {
        while (bfs(s, t, delta)) {
            std::fill(ptr_.begin(), ptr_.end(), 0);
            while (std::int64_t pushed = dfs(s, t, std::numeric_limits<std::int64_t>::max(), delta)) {
                flow += pushed;
            }
        }
    }
    return flow;
}

} // namespace codes_dinic_scaling_maxflow
