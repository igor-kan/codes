#include "interface.hpp"

namespace codes_stochastic_universal_sampl {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("stochastic_universal_sampl: problem size must be positive");
    }
}

} // namespace codes_stochastic_universal_sampl
