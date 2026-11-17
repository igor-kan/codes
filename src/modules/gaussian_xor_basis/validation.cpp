#include "interface.hpp"

namespace codes_gaussian_xor_basis {
void validate_kth(int rank, std::uint64_t k) {
    if (rank < 62 && k >= (1ULL << rank)) {
        throw std::out_of_range("kth_smallest index exceeds 2^rank");
    }
}
} // namespace codes_gaussian_xor_basis
