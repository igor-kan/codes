#include "interface.hpp"

namespace codes_polygonal_ear_clipping {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("polygonal_ear_clipping: problem size must be positive");
    }
}

} // namespace codes_polygonal_ear_clipping
