#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_z_algorithm_lcp {
std::vector<std::size_t> compute_z_array(const std::string& s);
std::vector<std::size_t> find_matches(const std::string& text, const std::string& pattern);
Status validate_inputs(const std::string& text, const std::string& pattern);
std::vector<std::size_t> compute_z_fast(const std::string& s);
std::vector<std::vector<std::size_t>> batch_find_matches(const std::vector<std::string>& texts, const std::string& pat);
Status verify_z_invariants(const std::string& s, const std::vector<std::size_t>& z);
} // namespace codes_z_algorithm_lcp
