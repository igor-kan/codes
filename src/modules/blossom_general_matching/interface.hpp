#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_blossom_general_matching {
MatchingResult edmonds_blossom_matching(int n, const std::vector<std::pair<int, int>>& edges);
void validate_matching_input(int n, const std::vector<std::pair<int, int>>& edges);
int fast_greedy_warm_match(int n, const std::vector<std::vector<int>>& adj, std::vector<int>& match);
std::vector<MatchingResult> parallel_matching_batch(const std::vector<std::pair<int, std::vector<std::pair<int, int>>>>& graphs);
void verify_matching_invariants(int n, const std::vector<std::pair<int, int>>& edges, const MatchingResult& res);
} // namespace codes_blossom_general_matching
