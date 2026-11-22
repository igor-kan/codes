#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_edmonds_karp_flow_d57 {
long long edmonds_karp_maxflow(int n, int s, int t, const std::vector<FlowEdgeSpec>& edges);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_edmonds_karp_flow_d57
