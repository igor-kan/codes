#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dominator_tree_lengauer;
    validate_problem_size(1);
    auto idom = compute_immediate_dominators(6, 0, {{0,1},{1,2},{1,3},{2,4},{3,4},{4,5}});
    assert(idom[4] == 1 && idom[5] == 4);
    assert(dominates(idom, 1, 5));
    verify_module_postcondition(true, "unit ok");
    return 0;
}
