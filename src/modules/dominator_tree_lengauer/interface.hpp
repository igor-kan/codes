#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_dominator_tree_lengauer {
std::vector<int> compute_immediate_dominators(int n, int root, const std::vector<std::pair<int, int>>& edges);
bool dominates(const std::vector<int>& idom, int u, int v);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_dominator_tree_lengauer
