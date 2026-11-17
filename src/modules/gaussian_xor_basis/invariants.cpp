#include "interface.hpp"

namespace codes_gaussian_xor_basis {
void verify_xor_basis_invariants(const XorBasis& b) {
    const auto& st = b.state();
    int cnt = 0;
    for (int bit = 0; bit < 62; ++bit) {
        std::uint64_t piv = st.basis[static_cast<std::size_t>(bit)];
        if (piv != 0) {
            if (((piv >> bit) & 1ULL) == 0 || (piv >> (bit + 1)) != 0) {
                throw std::logic_error("XOR basis pivot highest-bit invariant violated");
            }
            ++cnt;
        }
    }
    if (cnt != st.rank) throw std::logic_error("rank count mismatch");
}
} // namespace codes_gaussian_xor_basis
