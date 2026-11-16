#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_closest_pair_divide_conquer {
struct Point2D {
    double x = 0.0;
    double y = 0.0;
    std::size_t id = 0;
};

struct PairResult {
    std::size_t i = 0;
    std::size_t j = 0;
    double dist_sq = 0.0;
};
} // namespace codes_closest_pair_divide_conquer
