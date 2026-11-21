#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_kmp_border_automaton_d56 {
std::vector<int> kmp_prefix_function(const std::string& pat);
std::vector<int> kmp_find_all(const std::string& text, const std::string& pat);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_kmp_border_automaton_d56
