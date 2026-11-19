#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_pollard_rho_brent_u128 {
bool is_prime_u64(std::uint64_t n);
std::vector<std::uint64_t> factorize_u64(std::uint64_t n);

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_pollard_rho_brent_u128
