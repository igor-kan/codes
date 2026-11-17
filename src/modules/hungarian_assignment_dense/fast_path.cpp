#include "interface.hpp"

namespace codes_hungarian_assignment_dense {
std::int64_t fast_eval_assignment(const std::vector<std::vector<std::int64_t>>& cost, const std::vector<int>& assign) {
    std::int64_t sum = 0;
    for (std::size_t r = 0; r < assign.size(); ++r) {
        sum += cost[r][static_cast<std::size_t>(assign[r])];
    }
    return sum;
}
} // namespace codes_hungarian_assignment_dense
