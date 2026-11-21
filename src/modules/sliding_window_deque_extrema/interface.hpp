#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_sliding_window_deque_extrema {
std::vector<long long> sliding_window_max(const std::vector<long long>& xs, int k);
std::vector<long long> sliding_window_min(const std::vector<long long>& xs, int k);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_sliding_window_deque_extrema
