#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_pollard_rho_brent_u128 {

static std::uint64_t mulmod(std::uint64_t a, std::uint64_t b, std::uint64_t m) {
    return static_cast<std::uint64_t>((static_cast<unsigned __int128>(a) * b) % m);
}
static std::uint64_t powmod(std::uint64_t b, std::uint64_t e, std::uint64_t m) {
    std::uint64_t r = 1; b %= m;
    while (e > 0) {
        if (e & 1ULL) r = mulmod(r, b, m);
        b = mulmod(b, b, m); e >>= 1;
    }
    return r;
}
bool is_prime_u64(std::uint64_t n) {
    if (n < 2) return false;
    for (std::uint64_t p : {2ULL, 3ULL, 5ULL, 7ULL, 11ULL, 13ULL, 17ULL, 19ULL, 23ULL, 29ULL, 31ULL, 37ULL}) {
        if (n == p) return true;
        if (n % p == 0) return false;
    }
    std::uint64_t d = n - 1; int s = 0;
    while ((d & 1ULL) == 0) { d >>= 1; ++s; }
    for (std::uint64_t a : {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL, 9780504ULL, 1795265022ULL}) {
        if (a % n == 0) continue;
        std::uint64_t x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool comp = true;
        for (int r = 1; r < s; ++r) {
            x = mulmod(x, x, n);
            if (x == n - 1) { comp = false; break; }
        }
        if (comp) return false;
    }
    return true;
}
static std::uint64_t rho_split(std::uint64_t n) {
    if ((n & 1ULL) == 0) return 2;
    for (std::uint64_t c = 1; c < n; ++c) {
        std::uint64_t y = 2, r = 1, q = 1, g = 1, x = 2, ys = 2;
        while (g == 1) {
            x = y;
            for (std::uint64_t i = 0; i < r; ++i) y = (mulmod(y, y, n) + c) % n;
            std::uint64_t k = 0;
            while (k < r && g == 1) {
                ys = y;
                for (std::uint64_t i = 0; i < std::min<std::uint64_t>(16ULL, r - k); ++i) {
                    y = (mulmod(y, y, n) + c) % n;
                    q = mulmod(q, x > y ? x - y : y - x, n);
                }
                g = std::gcd(q, n); k += 16ULL;
            }
            r <<= 1;
        }
        if (g == n) do { ys = (mulmod(ys, ys, n) + c) % n; g = std::gcd(x > ys ? x - ys : ys - x, n); } while (g == 1);
        if (g != n) return g;
    }
    return n;
}
std::vector<std::uint64_t> factorize_u64(std::uint64_t n) {
    std::vector<std::uint64_t> out, st;
    if (n > 1) st.push_back(n);
    while (!st.empty()) {
        std::uint64_t v = st.back(); st.pop_back();
        if (is_prime_u64(v)) out.push_back(v);
        else { std::uint64_t d = rho_split(v); st.push_back(d); st.push_back(v / d); }
    }
    std::sort(out.begin(), out.end());
    return out;
}

} // namespace codes_pollard_rho_brent_u128
