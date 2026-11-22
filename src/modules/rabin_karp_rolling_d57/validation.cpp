#include "interface.hpp"

namespace codes_rabin_karp_rolling_d57 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("rabin_karp_rolling_d57: problem size must be positive");
    }
}

} // namespace codes_rabin_karp_rolling_d57
