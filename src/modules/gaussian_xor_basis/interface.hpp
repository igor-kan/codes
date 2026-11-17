#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_gaussian_xor_basis {
class XorBasis {
public:
    XorBasis() = default;
    bool insert(std::uint64_t x);
    bool can_represent(std::uint64_t x) const;
    std::uint64_t max_xor(std::uint64_t seed = 0) const;
    std::uint64_t kth_smallest(std::uint64_t k) const;
    void merge(const XorBasis& other);
    int rank() const { return state_.rank; }
    const XorBasisState& state() const { return state_; }

private:
    XorBasisState state_;
};

void validate_kth(int rank, std::uint64_t k);
std::uint64_t fast_batch_max_xor(const XorBasis& b, const std::vector<std::uint64_t>& seeds);
std::vector<std::uint64_t> parallel_basis_max_queries(const std::vector<std::uint64_t>& nums,
                                                      const std::vector<std::uint64_t>& seeds);
void verify_xor_basis_invariants(const XorBasis& b);
} // namespace codes_gaussian_xor_basis
