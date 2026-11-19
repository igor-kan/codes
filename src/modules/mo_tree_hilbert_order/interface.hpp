#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_mo_tree_hilbert_order {
std::uint64_t hilbert_order(int x, int y, int pow2_log);
std::vector<int> mo_distinct_queries(const std::vector<int>& arr, const std::vector<std::pair<int, int>>& qs);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_mo_tree_hilbert_order
