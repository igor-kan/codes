#include "interface.hpp"
namespace codes_topological_kahn_dag {
std::vector<std::size_t> compute_in_degrees(std::size_t n, const std::vector<std::vector<std::size_t>>& adj) {
    std::vector<std::size_t> indeg(n, 0);
    for (const auto& row : adj) for (std::size_t v : row) indeg[v]++;
    return indeg;
}
} // namespace codes_topological_kahn_dag
