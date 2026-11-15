#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_miller_rabin_primality {
struct PrimalityStats {
    std::size_t bases_tested = 0;
    bool is_prime = false;
};
} // namespace codes_miller_rabin_primality
