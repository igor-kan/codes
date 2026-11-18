#include "interface.hpp"

namespace codes_cartesian_tree_rmq_lca {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("cartesian_tree_rmq_lca: problem size must be positive");
    }
}

} // namespace codes_cartesian_tree_rmq_lca
