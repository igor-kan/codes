#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_matrix_path_count_d59 {
std::vector<std::vector<long long>> count_k_walks(const std::vector<std::vector<long long>>& adj, long long k);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_matrix_path_count_d59
