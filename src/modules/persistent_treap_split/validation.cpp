#include "interface.hpp"

namespace codes_persistent_treap_split {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("persistent_treap_split: problem size must be positive");
    }
}

} // namespace codes_persistent_treap_split
