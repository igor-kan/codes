#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_euler_tour_subtree_d59;
    validate_problem_size(1);
    auto ss = all_subtree_sums(4, 0, {10, 20, 30, 40}, {{0,1},{0,2},{1,3}});
    assert(ss[0] == 100 && ss[1] == 60 && ss[2] == 30 && ss[3] == 40);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
