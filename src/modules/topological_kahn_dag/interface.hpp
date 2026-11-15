#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_topological_kahn_dag {
TopoResult kahn_sort(std::size_t n, const std::vector<std::vector<std::size_t>>& adj);
TopoResult kahn_lex_min(std::size_t n, const std::vector<std::vector<std::size_t>>& adj);
Status validate_dag_inputs(std::size_t n, const std::vector<std::vector<std::size_t>>& adj);
std::vector<std::size_t> compute_in_degrees(std::size_t n, const std::vector<std::vector<std::size_t>>& adj);
std::vector<std::vector<std::size_t>> kahn_level_waves(std::size_t n, const std::vector<std::vector<std::size_t>>& adj);
Status verify_topological_order(std::size_t n, const std::vector<std::vector<std::size_t>>& adj, const TopoResult& res);
} // namespace codes_topological_kahn_dag
