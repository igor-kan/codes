#include "interface.hpp"

namespace codes_ntt_number_theoretic {
void validate_poly_inputs(const std::vector<std::uint64_t>& a, const std::vector<std::uint64_t>& b) {
    if (a.empty() || b.empty()) {
        throw std::invalid_argument("polynomial operand cannot be empty");
    }
}
} // namespace codes_ntt_number_theoretic
