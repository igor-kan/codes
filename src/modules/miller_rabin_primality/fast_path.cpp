#include "interface.hpp"
namespace codes_miller_rabin_primality {
bool passes_small_sieve(std::uint64_t n) {
    if (n < 2) return false;
    if (n == 2 || n == 3 || n == 5) return true;
    return (n % 2 != 0) && (n % 3 != 0) && (n % 5 != 0);
}
} // namespace codes_miller_rabin_primality
