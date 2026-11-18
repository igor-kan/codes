#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_directed_mst_chu_liu {
std::int64_t edmonds_directed_mst(int n, int root, std::vector<DirEdge> edges);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_directed_mst_chu_liu
