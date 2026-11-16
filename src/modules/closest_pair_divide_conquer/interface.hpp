#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_closest_pair_divide_conquer {
PairResult closest_pair_dc(std::vector<Point2D> pts);
Status validate_points(const std::vector<Point2D>& pts);
PairResult closest_pair_bruteforce(const std::vector<Point2D>& pts);
std::vector<PairResult> batch_closest_pairs(const std::vector<std::vector<Point2D>>& clouds);
Status verify_closest_pair_invariants(const std::vector<Point2D>& pts, const PairResult& res);
} // namespace codes_closest_pair_divide_conquer
