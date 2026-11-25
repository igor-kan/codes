#include "interface.hpp"

namespace codes_fenwick_2d_bit_d60 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("fenwick_2d_bit_d60: problem size must be positive");
    }
}

} // namespace codes_fenwick_2d_bit_d60
