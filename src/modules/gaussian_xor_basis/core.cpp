#include "interface.hpp"

namespace codes_gaussian_xor_basis {

bool XorBasis::insert(std::uint64_t x) {
    x &= ((1ULL << 62) - 1);
    for (int bit = 61; bit >= 0; --bit) {
        if ((x >> bit) & 1ULL) {
            if (state_.basis[static_cast<std::size_t>(bit)] == 0) {
                state_.basis[static_cast<std::size_t>(bit)] = x;
                ++state_.rank;
                return true;
            }
            x ^= state_.basis[static_cast<std::size_t>(bit)];
        }
    }
    return false;
}

bool XorBasis::can_represent(std::uint64_t x) const {
    x &= ((1ULL << 62) - 1);
    for (int bit = 61; bit >= 0; --bit) {
        if ((x >> bit) & 1ULL) {
            std::uint64_t piv = state_.basis[static_cast<std::size_t>(bit)];
            if (piv == 0) return false;
            x ^= piv;
        }
    }
    return x == 0;
}

std::uint64_t XorBasis::max_xor(std::uint64_t seed) const {
    std::uint64_t res = seed & ((1ULL << 62) - 1);
    for (int bit = 61; bit >= 0; --bit) {
        std::uint64_t piv = state_.basis[static_cast<std::size_t>(bit)];
        if ((res ^ piv) > res) res ^= piv;
    }
    return res;
}

std::uint64_t XorBasis::kth_smallest(std::uint64_t k) const {
    validate_kth(state_.rank, k);
    std::array<std::uint64_t, 62> diag = state_.basis;
    std::vector<std::uint64_t> pivots;
    for (int bit = 0; bit < 62; ++bit) {
        if (diag[static_cast<std::size_t>(bit)] != 0) {
            for (int hi = bit + 1; hi < 62; ++hi) {
                if ((diag[static_cast<std::size_t>(hi)] >> bit) & 1ULL) {
                    diag[static_cast<std::size_t>(hi)] ^= diag[static_cast<std::size_t>(bit)];
                }
            }
        }
    }
    for (int bit = 0; bit < 62; ++bit) {
        if (diag[static_cast<std::size_t>(bit)] != 0) pivots.push_back(diag[static_cast<std::size_t>(bit)]);
    }
    std::uint64_t ans = 0;
    for (std::size_t i = 0; i < pivots.size(); ++i) {
        if ((k >> i) & 1ULL) ans ^= pivots[i];
    }
    return ans;
}

void XorBasis::merge(const XorBasis& other) {
    for (int bit = 61; bit >= 0; --bit) {
        std::uint64_t v = other.state_.basis[static_cast<std::size_t>(bit)];
        if (v != 0) insert(v);
    }
}

} // namespace codes_gaussian_xor_basis
