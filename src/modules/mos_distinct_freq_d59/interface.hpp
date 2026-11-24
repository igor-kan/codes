#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_mos_distinct_freq_d59 {
std::vector<long long> count_equal_pairs_queries(const std::vector<int>& xs, const std::vector<std::pair<int, int>>& qs);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_mos_distinct_freq_d59
