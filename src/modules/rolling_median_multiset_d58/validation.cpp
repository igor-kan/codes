#include "interface.hpp"

namespace codes_rolling_median_multiset_d58 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("rolling_median_multiset_d58: problem size must be positive");
    }
}

} // namespace codes_rolling_median_multiset_d58
