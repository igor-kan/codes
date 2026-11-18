#include "interface.hpp"

namespace codes_directed_mst_chu_liu {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("directed_mst_chu_liu: problem size must be positive");
    }
}

} // namespace codes_directed_mst_chu_liu
