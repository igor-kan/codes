#include "interface.hpp"
#include <limits>

namespace codes_closest_pair_divide_conquer {
PairResult closest_pair_bruteforce(const std::vector<Point2D>& pts) {
    if (validate_points(pts) != Status::Ok) return {};
    PairResult best{0, 1, std::numeric_limits<double>::infinity()};
    for (std::size_t i = 0; i < pts.size(); ++i) {
        for (std::size_t j = i + 1; j < pts.size(); ++j) {
            double dx = pts[i].x - pts[j].x;
            double dy = pts[i].y - pts[j].y;
            double d = dx * dx + dy * dy;
            if (d < best.dist_sq) best = {i, j, d};
        }
    }
    return best;
}
} // namespace codes_closest_pair_divide_conquer
