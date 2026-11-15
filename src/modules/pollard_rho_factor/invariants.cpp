#include "interface.hpp"
namespace codes_pollard_rho_factor {
Status verify_factorization(std::uint64_t n, const std::vector<std::uint64_t>& f) {
    unsigned __int128 prod = 1;
    for (std::uint64_t p : f) {
        if (!is_prime_fast(p)) return Status::InvariantViolation;
        prod *= p;
    }
    return (prod == n) ? Status::Ok : Status::InvariantViolation;
}
} // namespace codes_pollard_rho_factor
