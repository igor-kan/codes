#include "interface.hpp"
namespace codes_topological_kahn_dag {
Status verify_topological_order(std::size_t n, const std::vector<std::vector<std::size_t>>& adj, const TopoResult& res) {
    if (!res.is_dag) return Status::Ok;
    if (res.order.size() != n) return Status::InvariantViolation;
    std::vector<std::size_t> pos(n, n);
    for (std::size_t i = 0; i < n; ++i) pos[res.order[i]] = i;
    for (std::size_t u = 0; u < n; ++u) {
        for (std::size_t v : adj[u]) if (pos[u] >= pos[v]) return Status::InvariantViolation;
    }
    return Status::Ok;
}
} // namespace codes_topological_kahn_dag
