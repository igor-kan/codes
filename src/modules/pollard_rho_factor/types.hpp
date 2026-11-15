#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_pollard_rho_factor {
struct FactorReport {
    std::uint64_t input = 0;
    std::vector<std::uint64_t> factors;
};
} // namespace codes_pollard_rho_factor
