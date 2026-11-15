#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_mo_offline_queries {
std::vector<std::size_t> answer_distinct_queries(const std::vector<int>& arr, const std::vector<RangeQuery>& queries);
std::vector<std::size_t> answer_brute_force(const std::vector<int>& arr, const std::vector<RangeQuery>& queries);
Status validate_queries(std::size_t n, const std::vector<RangeQuery>& queries);
Status verify_agreement(const std::vector<int>& arr, const std::vector<RangeQuery>& queries);
} // namespace codes_mo_offline_queries
