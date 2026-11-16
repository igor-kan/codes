#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_hierholzer_eulerian_circuit {
EulerResult find_directed_euler(std::size_t n, const std::vector<DirectedEdge>& edges);
Status validate_euler_input(std::size_t n, const std::vector<DirectedEdge>& edges);
EulerResult find_directed_euler_fast(std::size_t n, const std::vector<DirectedEdge>& edges);
std::vector<EulerResult> batch_directed_euler(const std::vector<std::pair<std::size_t, std::vector<DirectedEdge>>>& cases);
Status verify_euler_invariants(std::size_t n, const std::vector<DirectedEdge>& edges, const EulerResult& res);
} // namespace codes_hierholzer_eulerian_circuit
