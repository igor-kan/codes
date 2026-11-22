#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_rabin_karp_rolling_d57 {
std::vector<int> rabin_karp_search(const std::string& text, const std::string& pat);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_rabin_karp_rolling_d57
