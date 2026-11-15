#include "interface.hpp"
#include <unordered_set>
namespace codes_mo_offline_queries {
std::vector<std::size_t> answer_brute_force(const std::vector<int>& arr, const std::vector<RangeQuery>& queries) {
    std::vector<std::size_t> out(queries.size(), 0);
    for (const auto& q : queries) {
        std::unordered_set<int> s;
        for (std::size_t i = q.l; i <= q.r; ++i) s.insert(arr[i]);
        out[q.id] = s.size();
    }
    return out;
}
} // namespace codes_mo_offline_queries
