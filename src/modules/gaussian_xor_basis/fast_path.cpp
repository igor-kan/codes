#include "interface.hpp"

namespace codes_gaussian_xor_basis {
std::uint64_t fast_batch_max_xor(const XorBasis& b, const std::vector<std::uint64_t>& seeds) {
    std::uint64_t best = 0;
    for (auto s : seeds) {
        std::uint64_t v = b.max_xor(s);
        if (v > best) best = v;
    }
    return best;
}
} // namespace codes_gaussian_xor_basis
