#include "interface.hpp"

namespace codes_hierholzer_eulerian_circuit {
Status validate_euler_input(std::size_t n, const std::vector<DirectedEdge>& edges) {
    if (n == 0) return Status::NullOrEmpty;
    for (const auto& e : edges) {
        if (e.u >= n || e.v >= n) return Status::OutOfBounds;
    }
    return Status::Ok;
}
} // namespace codes_hierholzer_eulerian_circuit
