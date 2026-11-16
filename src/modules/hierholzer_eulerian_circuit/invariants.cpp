#include "interface.hpp"

namespace codes_hierholzer_eulerian_circuit {
Status verify_euler_invariants(std::size_t n, const std::vector<DirectedEdge>& edges, const EulerResult& res) {
    if (!res.valid) return Status::InvalidInput;
    if (res.edge_ids.size() != edges.size()) return Status::InvariantViolation;
    if (res.vertices.size() != edges.size() + 1) return Status::InvariantViolation;
    std::vector<bool> seen(edges.size(), false);
    for (std::size_t i = 0; i < edges.size(); ++i) {
        std::size_t eid = res.edge_ids[i];
        if (eid >= edges.size() || seen[eid]) return Status::InvariantViolation;
        seen[eid] = true;
        if (edges[eid].u >= n || edges[eid].v >= n) return Status::OutOfBounds;
        if (edges[eid].u != res.vertices[i] || edges[eid].v != res.vertices[i + 1]) {
            return Status::InvariantViolation;
        }
    }
    return Status::Ok;
}
} // namespace codes_hierholzer_eulerian_circuit
