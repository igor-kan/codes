#include "interface.hpp"

namespace codes_dominator_tree_lengauer {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("dominator_tree_lengauer: problem size must be positive");
    }
}

} // namespace codes_dominator_tree_lengauer
