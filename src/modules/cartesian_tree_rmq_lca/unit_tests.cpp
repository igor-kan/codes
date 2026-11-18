#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_cartesian_tree_rmq_lca;
    validate_problem_size(1);
    std::vector<std::int64_t> a = {9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5};
    CartesianTree ct(a);
    assert(ct.root() == 3);
    assert(ct.rmq_index(0, 2) == 1);
    assert(ct.rmq_index(4, 10) == 10);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
