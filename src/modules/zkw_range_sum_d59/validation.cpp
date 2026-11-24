#include "interface.hpp"

namespace codes_zkw_range_sum_d59 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("zkw_range_sum_d59: problem size must be positive");
    }
}

} // namespace codes_zkw_range_sum_d59
