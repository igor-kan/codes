#include "interface.hpp"
namespace codes_kosaraju_two_pass_scc {
Status validate_edges(std::size_t n, const std::vector<std::vector<std::size_t>>& adj) {
    if (adj.size() != n) return Status::OutOfBounds;
    for (const auto& row : adj) {
        for (std::size_t v : row) if (v >= n) return Status::OutOfBounds;
    }
    return Status::Ok;
}
} // namespace codes_kosaraju_two_pass_scc
