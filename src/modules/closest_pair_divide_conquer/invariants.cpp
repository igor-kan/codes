#include "interface.hpp"
#include <cmath>

namespace codes_closest_pair_divide_conquer {
Status verify_closest_pair_invariants(const std::vector<Point2D>& pts, const PairResult& res) {
    if (validate_points(pts) != Status::Ok) return Status::InvalidInput;
    if (res.i >= pts.size() || res.j >= pts.size() || res.i == res.j) return Status::OutOfBounds;
    double dx = pts[res.i].x - pts[res.j].x;
    double dy = pts[res.i].y - pts[res.j].y;
    if (std::abs((dx * dx + dy * dy) - res.dist_sq) > 1e-9) return Status::InvariantViolation;
    auto oracle = closest_pair_bruteforce(pts);
    if (std::abs(oracle.dist_sq - res.dist_sq) > 1e-9) return Status::InvariantViolation;
    return Status::Ok;
}
} // namespace codes_closest_pair_divide_conquer
