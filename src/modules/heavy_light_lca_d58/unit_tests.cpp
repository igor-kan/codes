#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_heavy_light_lca_d58;
    validate_problem_size(1);
    BinaryLiftLca bl(6, 0, {{0,1},{0,2},{1,3},{1,4},{2,5}});
    assert(bl.lca(3, 4) == 1 && bl.lca(3, 5) == 0);
    assert(bl.dist(3, 5) == 4);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
