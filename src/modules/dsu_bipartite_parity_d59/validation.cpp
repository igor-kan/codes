#include "interface.hpp"

namespace codes_dsu_bipartite_parity_d59 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("dsu_bipartite_parity_d59: problem size must be positive");
    }
}

} // namespace codes_dsu_bipartite_parity_d59
