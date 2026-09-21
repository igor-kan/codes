#include <iostream>
#include <cassert>
#include <cmath>
#include "kdtree_spatial_index.hpp"

int main() {
    std::vector<KDPoint> pts = {{0.0, 0.0}, {1.0, 1.0}, {10.0, 10.0}};
    KDTree tree(pts);
    KDPoint near = tree.find_nearest({1.1, 0.9});
    assert(std::fabs(near.x - 1.0) < 1e-6);
    std::cout << "test_kdtree_spatial_index PASSED\n";
    return 0;
}
