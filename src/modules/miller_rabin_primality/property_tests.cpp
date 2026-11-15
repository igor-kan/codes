#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_miller_rabin_primality;
    // All products of two >1 primes must be composite
    std::uint64_t p1 = 1000000007ULL, p2 = 1000000009ULL;
    assert(is_prime_u64(p1) && is_prime_u64(p2));
    assert(!is_prime_u64(p1 * p2));
    return 0;
}
