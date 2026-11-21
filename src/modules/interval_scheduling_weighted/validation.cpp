#include "interface.hpp"

namespace codes_interval_scheduling_weighted {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("interval_scheduling_weighted: problem size must be positive");
    }
}

} // namespace codes_interval_scheduling_weighted
