#include "interface.hpp"

namespace codes_bridges_articulation_lowlink {
Status validate_graph(std::size_t n, const std::vector<UndirectedEdge>& edges) {
    if (n == 0) return Status::NullOrEmpty;
    for (const auto& e : edges) {
        if (e.u >= n || e.v >= n) return Status::OutOfBounds;
    }
    return Status::Ok;
}
} // namespace codes_bridges_articulation_lowlink
