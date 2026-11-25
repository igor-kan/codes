#include "interface.hpp"

namespace codes_dinic_max_flow_d60 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("dinic_max_flow_d60: problem size must be positive");
    }
}

} // namespace codes_dinic_max_flow_d60
