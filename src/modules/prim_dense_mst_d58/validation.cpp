#include "interface.hpp"

namespace codes_prim_dense_mst_d58 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("prim_dense_mst_d58: problem size must be positive");
    }
}

} // namespace codes_prim_dense_mst_d58
