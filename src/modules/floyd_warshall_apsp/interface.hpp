#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_floyd_warshall_apsp {
ApspResult solve_apsp(std::size_t n, const std::vector<double>& adj_weights);
std::vector<int> reconstruct_path(const ApspResult& res, std::size_t u, std::size_t v);
Status validate_matrix(std::size_t n, const std::vector<double>& adj);
ApspResult solve_apsp_blocked(std::size_t n, const std::vector<double>& adj_weights);
Status batch_verify_paths(const ApspResult& res);
Status verify_triangle_inequality(const ApspResult& res);
} // namespace codes_floyd_warshall_apsp
