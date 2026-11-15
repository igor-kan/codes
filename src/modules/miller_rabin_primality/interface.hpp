#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_miller_rabin_primality {
std::uint64_t mul_mod_u64(std::uint64_t a, std::uint64_t b, std::uint64_t mod);
std::uint64_t pow_mod_u64(std::uint64_t base, std::uint64_t exp, std::uint64_t mod);
bool is_prime_u64(std::uint64_t n);
bool is_prime_trial(std::uint64_t n);
std::vector<std::uint64_t> filter_primes_mt(const std::vector<std::uint64_t>& nums);
Status verify_primality_agreement(std::uint64_t limit);
} // namespace codes_miller_rabin_primality
