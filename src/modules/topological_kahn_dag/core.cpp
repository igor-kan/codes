#include "interface.hpp"
#include <queue>

namespace codes_topological_kahn_dag {
TopoResult kahn_sort(std::size_t n, const std::vector<std::vector<std::size_t>>& adj) {
    TopoResult res;
    std::vector<std::size_t> indeg(n, 0);
    for (std::size_t u = 0; u < n; ++u) for (std::size_t v : adj[u]) indeg[v]++;
    std::queue<std::size_t> q;
    for (std::size_t i = 0; i < n; ++i) if (indeg[i] == 0) q.push(i);
    res.order.reserve(n);
    while (!q.empty()) {
        std::size_t u = q.front(); q.pop();
        res.order.push_back(u);
        for (std::size_t v : adj[u]) if (--indeg[v] == 0) q.push(v);
    }
    res.is_dag = (res.order.size() == n);
    return res;
}

TopoResult kahn_lex_min(std::size_t n, const std::vector<std::vector<std::size_t>>& adj) {
    TopoResult res;
    std::vector<std::size_t> indeg(n, 0);
    for (std::size_t u = 0; u < n; ++u) for (std::size_t v : adj[u]) indeg[v]++;
    std::priority_queue<std::size_t, std::vector<std::size_t>, std::greater<std::size_t>> pq;
    for (std::size_t i = 0; i < n; ++i) if (indeg[i] == 0) pq.push(i);
    while (!pq.empty()) {
        std::size_t u = pq.top(); pq.pop();
        res.order.push_back(u);
        for (std::size_t v : adj[u]) if (--indeg[v] == 0) pq.push(v);
    }
    res.is_dag = (res.order.size() == n);
    return res;
}
} // namespace codes_topological_kahn_dag
