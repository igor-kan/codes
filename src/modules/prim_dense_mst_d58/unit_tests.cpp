#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_prim_dense_mst_d58;
    validate_problem_size(1);
    std::vector<std::vector<long long>> m = {
        {0, 2, 6, 9},
        {2, 0, 3, 8},
        {6, 3, 0, 4},
        {9, 8, 4, 0}
    };
    assert(prim_dense_mst(m) == 9);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
