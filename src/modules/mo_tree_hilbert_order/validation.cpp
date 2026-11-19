#include "interface.hpp"

namespace codes_mo_tree_hilbert_order {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("mo_tree_hilbert_order: problem size must be positive");
    }
}

} // namespace codes_mo_tree_hilbert_order
