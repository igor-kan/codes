#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_longest_increasing_subseq_patience {
struct LisResult {
    std::vector<std::size_t> indices;
    std::vector<int64_t> values;
};
} // namespace codes_longest_increasing_subseq_patience
