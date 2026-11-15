#include "interface.hpp"
namespace codes_mo_offline_queries {
Status verify_agreement(const std::vector<int>& arr, const std::vector<RangeQuery>& queries) {
    auto a = answer_distinct_queries(arr, queries);
    auto b = answer_brute_force(arr, queries);
    return (a == b) ? Status::Ok : Status::InvariantViolation;
}
} // namespace codes_mo_offline_queries
