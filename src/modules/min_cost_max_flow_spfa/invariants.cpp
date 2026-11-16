#include "interface.hpp"

namespace codes_min_cost_max_flow_spfa {
Status verify_flow_invariants(std::size_t n, std::size_t src, std::size_t dst, const std::vector<FlowArc>& arcs, const FlowSolution& sol) {
    if (validate_flow_network(n, src, dst, arcs) != Status::Ok) return Status::InvalidInput;
    if (sol.arc_flows.size() != arcs.size()) return Status::InvariantViolation;
    std::vector<int64_t> net(n, 0);
    int64_t cost_sum = 0;
    for (std::size_t i = 0; i < arcs.size(); ++i) {
        int64_t f = sol.arc_flows[i];
        if (f < 0 || f > arcs[i].cap) return Status::InvariantViolation;
        net[arcs[i].from] += f;
        net[arcs[i].to] -= f;
        cost_sum += f * arcs[i].cost;
    }
    if (cost_sum != sol.total_cost) return Status::InvariantViolation;
    if (net[src] != sol.total_flow || net[dst] != -sol.total_flow) return Status::InvariantViolation;
    for (std::size_t v = 0; v < n; ++v) {
        if (v != src && v != dst && net[v] != 0) return Status::InvariantViolation;
    }
    return Status::Ok;
}
} // namespace codes_min_cost_max_flow_spfa
