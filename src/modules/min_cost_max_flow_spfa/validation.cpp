#include "interface.hpp"

namespace codes_min_cost_max_flow_spfa {
Status validate_flow_network(std::size_t n, std::size_t src, std::size_t dst, const std::vector<FlowArc>& arcs) {
    if (n < 2) return Status::NullOrEmpty;
    if (src >= n || dst >= n || src == dst) return Status::InvalidInput;
    for (const auto& a : arcs) {
        if (a.from >= n || a.to >= n) return Status::OutOfBounds;
        if (a.cap < 0 || a.cost < 0) return Status::InvalidInput;
    }
    return Status::Ok;
}
} // namespace codes_min_cost_max_flow_spfa
