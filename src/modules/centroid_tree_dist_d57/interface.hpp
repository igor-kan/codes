#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_centroid_tree_dist_d57 {
TreeExtent compute_tree_extent(int n, const std::vector<std::pair<int, int>>& edges);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_centroid_tree_dist_d57
