#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_centroid_tree_dist_d57;
    validate_problem_size(1);
    auto ext = compute_tree_extent(5, {{0,1},{1,2},{2,3},{3,4}});
    assert(ext.diameter == 4 && ext.radius == 2);
    auto star = compute_tree_extent(5, {{0,1},{0,2},{0,3},{0,4}});
    assert(star.diameter == 2 && star.radius == 1);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
