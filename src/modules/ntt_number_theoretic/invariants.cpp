#include "interface.hpp"

namespace codes_ntt_number_theoretic {
void verify_ntt_exactness(const std::vector<std::uint64_t>& a, const std::vector<std::uint64_t>& b) {
    auto fast = ntt_convolve(a, b);
    auto ref = naive_convolve(a, b);
    if (fast != ref) throw std::logic_error("NTT convolution disagreed with naive Cauchy product");
}
} // namespace codes_ntt_number_theoretic
