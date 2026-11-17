#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_gomory_hu_cut_tree {
std::vector<GhEdge> build_gomory_hu_tree(int n, const std::vector<UndirectedEdge>& edges);
std::int64_t query_pair_min_cut(int n, const std::vector<GhEdge>& tree, int s, int t);
void validate_graph(int n, const std::vector<UndirectedEdge>& edges);
std::vector<std::int64_t> fast_all_pairs_cuts(int n, const std::vector<GhEdge>& tree);
std::vector<std::int64_t> parallel_cut_queries(int n, const std::vector<UndirectedEdge>& edges,
                                               const std::vector<std::pair<int, int>>& pairs);
void verify_gomory_hu_parity(int n, const std::vector<UndirectedEdge>& edges, const std::vector<GhEdge>& tree);
} // namespace codes_gomory_hu_cut_tree
