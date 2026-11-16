#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_min_cost_max_flow_spfa {
FlowSolution solve_mcmf_spfa(std::size_t n, std::size_t src, std::size_t dst, const std::vector<FlowArc>& arcs);
Status validate_flow_network(std::size_t n, std::size_t src, std::size_t dst, const std::vector<FlowArc>& arcs);
FlowSolution solve_mcmf_potentials(std::size_t n, std::size_t src, std::size_t dst, const std::vector<FlowArc>& arcs);
std::vector<FlowSolution> batch_mcmf(const std::vector<std::tuple<std::size_t, std::size_t, std::size_t, std::vector<FlowArc>>>& tasks);
Status verify_flow_invariants(std::size_t n, std::size_t src, std::size_t dst, const std::vector<FlowArc>& arcs, const FlowSolution& sol);
} // namespace codes_min_cost_max_flow_spfa
