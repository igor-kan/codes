#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_bellman_ford_spfa_d57 {
std::pair<bool, std::vector<long long>> bellman_ford_solve(int n, int src, const std::vector<DirWeightedEdge>& edges);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_bellman_ford_spfa_d57
