#include "interface.hpp"

namespace codes_sliding_window_deque_extrema {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("sliding_window_deque_extrema: problem size must be positive");
    }
}

} // namespace codes_sliding_window_deque_extrema
