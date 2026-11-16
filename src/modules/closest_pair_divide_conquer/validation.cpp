#include "interface.hpp"
#include <cmath>

namespace codes_closest_pair_divide_conquer {
Status validate_points(const std::vector<Point2D>& pts) {
    if (pts.size() < 2) return Status::InvalidInput;
    for (const auto& p : pts) {
        if (!std::isfinite(p.x) || !std::isfinite(p.y)) return Status::NumericError;
    }
    return Status::Ok;
}
} // namespace codes_closest_pair_divide_conquer
