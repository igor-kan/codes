#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_gaussian_xor_basis {
struct XorBasisState {
    std::array<std::uint64_t, 62> basis{};
    int rank = 0;
};
} // namespace codes_gaussian_xor_basis
