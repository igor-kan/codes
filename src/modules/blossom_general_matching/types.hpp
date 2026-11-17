#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_blossom_general_matching {
struct MatchingResult {
    int pairs;
    std::vector<int> partner;
};
} // namespace codes_blossom_general_matching
