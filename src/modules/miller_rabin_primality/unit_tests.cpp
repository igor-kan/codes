#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_miller_rabin_primality;
    assert(verify_primality_agreement(5000) == Status::Ok);
    assert(is_prime_u64(2305843009213693951ULL));  // Mersenne M61
    assert(!is_prime_u64(18446744073709551615ULL)); // 2^64 - 1 (composite)
    assert(is_prime_u64(18446744073709551557ULL));  // Largest 64-bit prime
    assert(!is_prime_u64(561) && !is_prime_u64(1729) && !is_prime_u64(341550071728321ULL)); // Carmichael numbers
    return 0;
}
