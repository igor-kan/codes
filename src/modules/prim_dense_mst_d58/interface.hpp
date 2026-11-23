#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_prim_dense_mst_d58 {
long long prim_dense_mst(const std::vector<std::vector<long long>>& mat);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_prim_dense_mst_d58
