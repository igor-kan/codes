#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_pollard_rho_factor {
std::uint64_t gcd_u64(std::uint64_t a, std::uint64_t b);
std::uint64_t rho_split_brent(std::uint64_t n);
std::vector<std::uint64_t> factorize_u64(std::uint64_t n);
bool is_prime_fast(std::uint64_t n);
Status verify_factorization(std::uint64_t n, const std::vector<std::uint64_t>& f);
} // namespace codes_pollard_rho_factor
