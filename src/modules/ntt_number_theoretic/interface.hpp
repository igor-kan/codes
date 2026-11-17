#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_ntt_number_theoretic {
std::uint64_t mod_pow(std::uint64_t base, std::uint64_t exp);
void ntt_transform(std::vector<std::uint64_t>& a, bool invert);
std::vector<std::uint64_t> ntt_convolve(const std::vector<std::uint64_t>& a, const std::vector<std::uint64_t>& b);
void validate_poly_inputs(const std::vector<std::uint64_t>& a, const std::vector<std::uint64_t>& b);
std::vector<std::uint64_t> naive_convolve(const std::vector<std::uint64_t>& a, const std::vector<std::uint64_t>& b);
std::vector<std::vector<std::uint64_t>> parallel_convolve_batch(
    const std::vector<std::pair<std::vector<std::uint64_t>, std::vector<std::uint64_t>>>& pairs);
void verify_ntt_exactness(const std::vector<std::uint64_t>& a, const std::vector<std::uint64_t>& b);
} // namespace codes_ntt_number_theoretic
