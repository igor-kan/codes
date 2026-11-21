#include "interface.hpp"

namespace codes_binary_indexed_fenwick_2d {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("binary_indexed_fenwick_2d: problem size must be positive");
    }
}

} // namespace codes_binary_indexed_fenwick_2d
