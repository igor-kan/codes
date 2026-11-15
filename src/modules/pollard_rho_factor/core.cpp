#include "interface.hpp"
#include <algorithm>

namespace codes_pollard_rho_factor {
static inline std::uint64_t mulm(std::uint64_t a, std::uint64_t b, std::uint64_t m) {
    return static_cast<std::uint64_t>((static_cast<unsigned __int128>(a) * b) % m);
}
static inline std::uint64_t powm(std::uint64_t b, std::uint64_t e, std::uint64_t m) {
    std::uint64_t r = 1 % m; b %= m;
    while (e) { if (e & 1ULL) r = mulm(r, b, m); b = mulm(b, b, m); e >>= 1; }
    return r;
}

std::uint64_t gcd_u64(std::uint64_t a, std::uint64_t b) {
    while (b) { std::uint64_t t = a % b; a = b; b = t; }
    return a;
}

bool is_prime_fast(std::uint64_t n) {
    if (n < 2) return false;
    static constexpr std::uint64_t b[12] = {2,3,5,7,11,13,17,19,23,29,31,37};
    for (auto p : b) { if (n == p) return true; if (n % p == 0) return false; }
    std::uint64_t d = n - 1; unsigned s = 0;
    while ((d & 1ULL) == 0) { d >>= 1; ++s; }
    for (auto a : b) {
        if (a >= n) break;
        std::uint64_t x = powm(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool comp = true;
        for (unsigned r = 1; r < s; ++r) { x = mulm(x, x, n); if (x == n - 1) { comp = false; break; } }
        if (comp) return false;
    }
    return true;
}

std::uint64_t rho_split_brent(std::uint64_t n) {
    if ((n & 1ULL) == 0) return 2;
    for (std::uint64_t c = 1; ; ++c) {
        std::uint64_t x = 2, y = 2, d = 1;
        auto f = [&](std::uint64_t v) { return (mulm(v, v, n) + c) % n; };
        while (d == 1) {
            x = f(x);
            y = f(f(y));
            std::uint64_t diff = x > y ? (x - y) : (y - x);
            d = gcd_u64(diff, n);
        }
        if (d < n) return d;
    }
}

static void rec_factor(std::uint64_t n, std::vector<std::uint64_t>& out) {
    if (n <= 1) return;
    if (is_prime_fast(n)) { out.push_back(n); return; }
    std::uint64_t d = rho_split_brent(n);
    rec_factor(d, out);
    rec_factor(n / d, out);
}

std::vector<std::uint64_t> factorize_u64(std::uint64_t n) {
    std::vector<std::uint64_t> out;
    if (n <= 1) return out;
    rec_factor(n, out);
    std::sort(out.begin(), out.end());
    return out;
}
} // namespace codes_pollard_rho_factor
