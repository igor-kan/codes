#include "interface.hpp"

namespace codes_lis_patience_sort_d57 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("lis_patience_sort_d57: problem size must be positive");
    }
}

} // namespace codes_lis_patience_sort_d57
