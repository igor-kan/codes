#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_centroid_decomposition_tree;
    CentroidOracle co(7, {{0,1},{1,2},{1,3},{0,4},{4,5},{5,6}});
    assert(co.nearest_active_dist(3) == -1);
    co.activate(0);
    assert(co.nearest_active_dist(3) == 2);
    assert(co.nearest_active_dist(6) == 3);
    co.activate(5);
    assert(co.nearest_active_dist(6) == 1);
    assert(co.nearest_active_dist(3) == 2);
    verify_centroid_depth(co.metadata(), 7);
    return 0;
}
