#include "interface.hpp"
namespace codes_topological_kahn_dag {
Status validate_dag_inputs(std::size_t n, const std::vector<std::vector<std::size_t>>& adj) {
    if (adj.size() != n) return Status::OutOfBounds;
    for (const auto& row : adj) for (std::size_t v : row) if (v >= n) return Status::OutOfBounds;
    return Status::Ok;
}
} // namespace codes_topological_kahn_dag
