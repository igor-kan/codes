#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_kosaraju_two_pass_scc {
SccResult find_scc(std::size_t n, const std::vector<std::vector<std::size_t>>& adj);
Status validate_edges(std::size_t n, const std::vector<std::vector<std::size_t>>& adj);
SccResult find_scc_iterative(std::size_t n, const std::vector<std::vector<std::size_t>>& adj);
Status verify_condensation_dag(std::size_t n, const std::vector<std::vector<std::size_t>>& adj, const SccResult& res);
} // namespace codes_kosaraju_two_pass_scc
