#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_dinic_max_flow_d60 {

DinicFlow::DinicFlow(int n) : n_(n), g_(n), level_(n), ptr_(n) {}
void DinicFlow::add_edge(int u, int v, std::int64_t cap) {
    FlowEdge a{v, static_cast<int>(g_[v].size()), cap};
    FlowEdge b{u, static_cast<int>(g_[u].size()), 0};
    g_[u].push_back(a);
    g_[v].push_back(b);
}
bool DinicFlow::bfs(int s, int t) {
    std::fill(level_.begin(), level_.end(), -1);
    level_[s] = 0;
    std::queue<int> q;
    q.push(s);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (const auto& e : g_[u]) {
            if (e.cap > 0 && level_[e.to] == -1) {
                level_[e.to] = level_[u] + 1;
                q.push(e.to);
            }
        }
    }
    return level_[t] != -1;
}
std::int64_t DinicFlow::dfs(int u, int t, std::int64_t pushed) {
    if (pushed == 0 || u == t) return pushed;
    for (int& cid = ptr_[u]; cid < static_cast<int>(g_[u].size()); ++cid) {
        auto& e = g_[u][cid];
        if (level_[e.to] != level_[u] + 1 || e.cap == 0) continue;
        std::int64_t tr = dfs(e.to, t, std::min(pushed, e.cap));
        if (tr == 0) continue;
        e.cap -= tr;
        g_[e.to][e.rev].cap += tr;
        return tr;
    }
    return 0;
}
std::int64_t DinicFlow::max_flow(int s, int t) {
    std::int64_t flow = 0;
    while (bfs(s, t)) {
        std::fill(ptr_.begin(), ptr_.end(), 0);
        while (std::int64_t pushed = dfs(s, t, 1000000000000000LL)) {
            flow += pushed;
        }
    }
    return flow;
}

} // namespace codes_dinic_max_flow_d60
