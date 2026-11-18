#include "interface.hpp"

namespace codes_min_enclosing_circle_welzl {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("min_enclosing_circle_welzl: problem size must be positive");
    }
}

} // namespace codes_min_enclosing_circle_welzl
