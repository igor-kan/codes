#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_z_algorithm_lcp {
struct ZConfig {
    std::size_t max_pattern_len = 1U << 20;
    bool include_overlapping = true;
};

struct ZMatchResult {
    std::vector<std::size_t> z_array;
    std::vector<std::size_t> match_offsets;
};
} // namespace codes_z_algorithm_lcp
