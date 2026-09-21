#include "kdtree_spatial_index.hpp"
#include <cmath>
#include <limits>

KDTree::KDTree(const std::vector<KDPoint>& points) : pts_(points) {}

KDPoint KDTree::find_nearest(const KDPoint& target) const {
    double best_dist = std::numeric_limits<double>::infinity();
    KDPoint best_pt = {0.0, 0.0};
    for (const auto& p : pts_) {
        double d = std::sqrt((p.x - target.x)*(p.x - target.x) + (p.y - target.y)*(p.y - target.y));
        if (d < best_dist) {
            best_dist = d;
            best_pt = p;
        }
    }
    return best_pt;
}
