#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_johnson_apsp_reweight {
JohnsonOutput solve_johnson(std::size_t n, const std::vector<std::vector<WEdge>>& adj);
Status validate_reweighting(const std::vector<std::vector<WEdge>>& adj, const std::vector<double>& h);
JohnsonOutput solve_johnson_mt(std::size_t n, const std::vector<std::vector<WEdge>>& adj);
Status verify_matrix_invariants(const JohnsonOutput& out);
} // namespace codes_johnson_apsp_reweight
