#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_closest_pair_divide_conquer;
    std::vector<Point2D> pts = {{0,0,0}, {3,4,1}, {1,1,2}, {5,5,3}, {1.1,1.0,4}, {-2,-3,5}};
    auto r = closest_pair_dc(pts);
    assert(std::abs(r.dist_sq - 0.01) < 1e-9);
    assert(verify_closest_pair_invariants(pts, r) == Status::Ok);

    std::vector<Point2D> dup = {{2,3,0},{5,6,1},{2,3,2}};
    auto r2 = closest_pair_dc(dup);
    assert(r2.dist_sq == 0.0);
    assert(verify_closest_pair_invariants(dup, r2) == Status::Ok);
    return 0;
}
