#include "interface.hpp"

namespace codes_edmonds_karp_flow_d57 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("edmonds_karp_flow_d57: problem size must be positive");
    }
}

} // namespace codes_edmonds_karp_flow_d57
