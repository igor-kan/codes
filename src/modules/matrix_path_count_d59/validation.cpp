#include "interface.hpp"

namespace codes_matrix_path_count_d59 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("matrix_path_count_d59: problem size must be positive");
    }
}

} // namespace codes_matrix_path_count_d59
