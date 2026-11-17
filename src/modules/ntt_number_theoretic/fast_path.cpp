#include "interface.hpp"

namespace codes_ntt_number_theoretic {
std::vector<std::uint64_t> naive_convolve(const std::vector<std::uint64_t>& a, const std::vector<std::uint64_t>& b) {
    std::vector<std::uint64_t> out(a.size() + b.size() - 1, 0);
    for (std::size_t i = 0; i < a.size(); ++i) {
        for (std::size_t j = 0; j < b.size(); ++j) {
            out[i + j] = (out[i + j] + (a[i] % NTT_MOD) * (b[j] % NTT_MOD)) % NTT_MOD;
        }
    }
    return out;
}
} // namespace codes_ntt_number_theoretic
