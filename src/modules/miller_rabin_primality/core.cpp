#include "interface.hpp"

namespace codes_miller_rabin_primality {
std::uint64_t mul_mod_u64(std::uint64_t a, std::uint64_t b, std::uint64_t mod) {
    return static_cast<std::uint64_t>((static_cast<unsigned __int128>(a) * b) % mod);
}

std::uint64_t pow_mod_u64(std::uint64_t base, std::uint64_t exp, std::uint64_t mod) {
    std::uint64_t res = 1 % mod;
    base %= mod;
    while (exp > 0) {
        if (exp & 1ULL) res = mul_mod_u64(res, base, mod);
        base = mul_mod_u64(base, base, mod);
        exp >>= 1;
    }
    return res;
}

bool is_prime_u64(std::uint64_t n) {
    if (n < 2) return false;
    static constexpr std::uint64_t bases[12] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (std::uint64_t p : bases) {
        if (n == p) return true;
        if (n % p == 0) return false;
    }
    std::uint64_t d = n - 1;
    unsigned s = 0;
    while ((d & 1ULL) == 0) { d >>= 1; ++s; }
    for (std::uint64_t a : bases) {
        if (a >= n) break;
        std::uint64_t x = pow_mod_u64(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (unsigned r = 1; r < s; ++r) {
            x = mul_mod_u64(x, x, n);
            if (x == n - 1) { composite = false; break; }
        }
        if (composite) return false;
    }
    return true;
}
} // namespace codes_miller_rabin_primality
