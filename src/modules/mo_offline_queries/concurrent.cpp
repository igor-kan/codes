#include "interface.hpp"
#include <thread>
namespace codes_mo_offline_queries {
std::vector<std::size_t> answer_parallel_halves(const std::vector<int>& arr, const std::vector<RangeQuery>& queries) {
    return answer_distinct_queries(arr, queries);
}
} // namespace codes_mo_offline_queries
