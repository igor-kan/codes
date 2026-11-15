#include "interface.hpp"
namespace codes_johnson_apsp_reweight {
Status validate_reweighting(const std::vector<std::vector<WEdge>>& adj, const std::vector<double>& h) {
    if (adj.size() != h.size()) return Status::OutOfBounds;
    for (std::size_t u = 0; u < adj.size(); ++u) {
        for (const auto& e : adj[u]) {
            if (e.w + h[u] - h[e.to] < -1e-9) return Status::InvariantViolation;
        }
    }
    return Status::Ok;
}
} // namespace codes_johnson_apsp_reweight
