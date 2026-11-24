#include "interface.hpp"

namespace codes_mos_distinct_freq_d59 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("mos_distinct_freq_d59: problem size must be positive");
    }
}

} // namespace codes_mos_distinct_freq_d59
