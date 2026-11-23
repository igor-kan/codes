#include "interface.hpp"

namespace codes_min_cost_max_flow_d58 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("min_cost_max_flow_d58: problem size must be positive");
    }
}

} // namespace codes_min_cost_max_flow_d58
