#include "interface.hpp"

namespace codes_hungarian_assignment_dense {
void validate_cost_matrix(const std::vector<std::vector<std::int64_t>>& cost) {
    if (cost.empty() || cost[0].empty()) throw std::invalid_argument("cost matrix cannot be empty");
    std::size_t cols = cost[0].size();
    if (cost.size() > cols) throw std::invalid_argument("rows cannot exceed columns");
    for (const auto& row : cost) {
        if (row.size() != cols) throw std::invalid_argument("ragged cost matrix");
    }
}
} // namespace codes_hungarian_assignment_dense
