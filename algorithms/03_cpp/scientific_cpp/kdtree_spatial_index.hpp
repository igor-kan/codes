#ifndef KDTREE_SPATIAL_INDEX_HPP
#define KDTREE_SPATIAL_INDEX_HPP

#include <vector>

struct KDPoint {
    double x, y;
};

class KDTree {
public:
    KDTree(const std::vector<KDPoint>& points);
    KDPoint find_nearest(const KDPoint& target) const;
private:
    std::vector<KDPoint> pts_;
};

#endif
