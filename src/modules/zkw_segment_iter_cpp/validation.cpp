#include "interface.hpp"

namespace codes_zkw_segment_iter_cpp {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("zkw_segment_iter_cpp: problem size must be positive");
    }
}

} // namespace codes_zkw_segment_iter_cpp
