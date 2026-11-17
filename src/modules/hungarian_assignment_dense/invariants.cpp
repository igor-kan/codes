#include "interface.hpp"
#include <set>

namespace codes_hungarian_assignment_dense {
void verify_assignment_valid(const std::vector<std::vector<std::int64_t>>& cost, const AssignmentSolution& sol) {
    if (sol.row_to_col.size() != cost.size()) throw std::logic_error("assignment size mismatch");
    std::set<int> used;
    for (int c : sol.row_to_col) {
        if (c < 0 || c >= static_cast<int>(cost[0].size()) || !used.insert(c).second) {
            throw std::logic_error("duplicate or out-of-range column");
        }
    }
    if (fast_eval_assignment(cost, sol.row_to_col) != sol.total_cost) {
        throw std::logic_error("cost sum mismatch");
    }
}
} // namespace codes_hungarian_assignment_dense
