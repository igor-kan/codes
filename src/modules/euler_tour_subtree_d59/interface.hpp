#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_euler_tour_subtree_d59 {
std::vector<long long> all_subtree_sums(int n, int root, const std::vector<long long>& weights, const std::vector<std::pair<int, int>>& edges);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_euler_tour_subtree_d59
