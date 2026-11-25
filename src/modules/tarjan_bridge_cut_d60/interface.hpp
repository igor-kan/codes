#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_tarjan_bridge_cut_d60 {
struct CutResult {
    std::vector<GraphEdge> bridges;
    std::vector<int> cut_vertices;
};
CutResult find_bridges_and_cuts(int n, const std::vector<GraphEdge>& edges);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_tarjan_bridge_cut_d60
