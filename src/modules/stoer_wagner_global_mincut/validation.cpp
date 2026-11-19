#include "interface.hpp"

namespace codes_stoer_wagner_global_mincut {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("stoer_wagner_global_mincut: problem size must be positive");
    }
}

} // namespace codes_stoer_wagner_global_mincut
