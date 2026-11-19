#include "interface.hpp"

namespace codes_pollard_rho_brent_u128 {

void validate_problem_size(int n) {
    if (n <= 0) {
        throw std::invalid_argument("pollard_rho_brent_u128: problem size must be positive");
    }
}

} // namespace codes_pollard_rho_brent_u128
