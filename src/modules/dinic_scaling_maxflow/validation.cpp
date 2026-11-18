#include "interface.hpp"

namespace codes_dinic_scaling_maxflow {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("dinic_scaling_maxflow: problem size must be positive");
    }
}

} // namespace codes_dinic_scaling_maxflow
