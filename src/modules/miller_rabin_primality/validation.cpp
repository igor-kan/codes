#include "interface.hpp"
namespace codes_miller_rabin_primality {
bool is_prime_trial(std::uint64_t n) {
    if (n < 2) return false;
    for (std::uint64_t d = 2; d * d <= n; ++d) if (n % d == 0) return false;
    return true;
}
} // namespace codes_miller_rabin_primality
