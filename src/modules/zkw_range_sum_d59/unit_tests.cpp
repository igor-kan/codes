#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_zkw_range_sum_d59;
    validate_problem_size(1);
    ZkwSumTree zkw(6);
    zkw.add(1, 10); zkw.add(3, 5); zkw.add(5, -2);
    assert(zkw.sum(1, 5) == 13 && zkw.sum(0, 2) == 10);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
