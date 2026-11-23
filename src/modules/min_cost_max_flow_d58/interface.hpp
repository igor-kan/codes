#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_min_cost_max_flow_d58 {
std::pair<long long, long long> min_cost_max_flow(int n, int s, int t, const std::vector<CostArc>& arcs);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_min_cost_max_flow_d58
