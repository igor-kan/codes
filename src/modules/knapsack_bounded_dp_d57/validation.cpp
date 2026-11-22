#include "interface.hpp"

namespace codes_knapsack_bounded_dp_d57 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("knapsack_bounded_dp_d57: problem size must be positive");
    }
}

} // namespace codes_knapsack_bounded_dp_d57
