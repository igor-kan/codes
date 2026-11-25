#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_fenwick_2d_bit_d60;
    validate_problem_size(1);
    Fenwick2D bit(4, 4);
    bit.add(1, 1, 5);
    bit.add(2, 3, 7);
    bit.add(0, 0, 2);
    assert(bit.rect_sum(1, 1, 2, 3) == 12);
    assert(bit.rect_sum(0, 0, 3, 3) == 14);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
