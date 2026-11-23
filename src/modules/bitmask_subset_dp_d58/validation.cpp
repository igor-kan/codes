#include "interface.hpp"

namespace codes_bitmask_subset_dp_d58 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("bitmask_subset_dp_d58: problem size must be positive");
    }
}

} // namespace codes_bitmask_subset_dp_d58
