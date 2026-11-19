#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_pollard_rho_brent_u128 {
struct FactorList {
    std::uint64_t n = 0;
    int num_factors = 0;
};

struct ModuleMeta {
    static constexpr const char* kSlug = "pollard_rho_brent_u128";
    int version = 1;
};
} // namespace codes_pollard_rho_brent_u128
