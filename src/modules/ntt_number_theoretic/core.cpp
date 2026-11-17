#include "interface.hpp"
#include <algorithm>

namespace codes_ntt_number_theoretic {

std::uint64_t mod_pow(std::uint64_t base, std::uint64_t exp) {
    std::uint64_t res = 1;
    base %= NTT_MOD;
    while (exp > 0) {
        if (exp & 1ULL) res = (res * base) % NTT_MOD;
        base = (base * base) % NTT_MOD;
        exp >>= 1;
    }
    return res;
}

void ntt_transform(std::vector<std::uint64_t>& a, bool invert) {
    std::size_t n = a.size();
    if (n == 0 || (n & (n - 1)) != 0) throw std::invalid_argument("NTT size must be a positive power of two");
    for (std::size_t i = 1, j = 0; i < n; ++i) {
        std::size_t bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) std::swap(a[i], a[j]);
    }
    std::uint64_t root_inv = mod_pow(NTT_ROOT, NTT_MOD - 2);
    for (std::size_t len = 2; len <= n; len <<= 1) {
        std::uint64_t wlen = mod_pow(invert ? root_inv : NTT_ROOT, (NTT_MOD - 1) / len);
        for (std::size_t i = 0; i < n; i += len) {
            std::uint64_t w = 1;
            for (std::size_t j = 0; j < len / 2; ++j) {
                std::uint64_t u = a[i + j];
                std::uint64_t v = (a[i + j + len / 2] * w) % NTT_MOD;
                a[i + j] = (u + v >= NTT_MOD) ? (u + v - NTT_MOD) : (u + v);
                a[i + j + len / 2] = (u >= v) ? (u - v) : (u + NTT_MOD - v);
                w = (w * wlen) % NTT_MOD;
            }
        }
    }
    if (invert) {
        std::uint64_t n_inv = mod_pow(n, NTT_MOD - 2);
        for (auto& x : a) x = (x * n_inv) % NTT_MOD;
    }
}

std::vector<std::uint64_t> ntt_convolve(const std::vector<std::uint64_t>& a, const std::vector<std::uint64_t>& b) {
    validate_poly_inputs(a, b);
    std::size_t need = a.size() + b.size() - 1;
    std::size_t n = 1;
    while (n < need) n <<= 1;
    std::vector<std::uint64_t> fa(n, 0), fb(n, 0);
    for (std::size_t i = 0; i < a.size(); ++i) fa[i] = a[i] % NTT_MOD;
    for (std::size_t i = 0; i < b.size(); ++i) fb[i] = b[i] % NTT_MOD;
    ntt_transform(fa, false);
    ntt_transform(fb, false);
    for (std::size_t i = 0; i < n; ++i) fa[i] = (fa[i] * fb[i]) % NTT_MOD;
    ntt_transform(fa, true);
    fa.resize(need);
    return fa;
}

} // namespace codes_ntt_number_theoretic
