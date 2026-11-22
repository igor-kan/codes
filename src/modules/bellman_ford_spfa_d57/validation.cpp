#include "interface.hpp"

namespace codes_bellman_ford_spfa_d57 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("bellman_ford_spfa_d57: problem size must be positive");
    }
}

} // namespace codes_bellman_ford_spfa_d57
