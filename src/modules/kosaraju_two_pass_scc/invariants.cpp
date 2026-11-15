#include "interface.hpp"
namespace codes_kosaraju_two_pass_scc {
Status verify_condensation_dag(std::size_t n, const std::vector<std::vector<std::size_t>>& adj, const SccResult& res) {
    if (res.comp_id.size() != n) return Status::InvariantViolation;
    for (std::size_t u = 0; u < n; ++u) {
        for (std::size_t v : adj[u]) {
            // Kosaraju produces reverse-postorder components so comp(u) <= comp(v)!
            if (res.comp_id[u] > res.comp_id[v]) return Status::InvariantViolation;
        }
    }
    return Status::Ok;
}
} // namespace codes_kosaraju_two_pass_scc
