#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_ahocorasick_automaton_d56 {
int ac_count_matches(const std::vector<std::string>& patterns, const std::string& text);
std::vector<int> ac_per_pattern_hits(const std::vector<std::string>& patterns, const std::string& text);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_ahocorasick_automaton_d56
