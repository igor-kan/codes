#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_binary_indexed_fenwick_2d;
    validate_problem_size(1);
    Fenwick2D fw(4, 4);
    fw.add(1, 1, 5);
    fw.add(2, 3, 7);
    fw.add(3, 2, -2);
    assert(fw.rect_sum(1, 1, 3, 3) == 10);
    assert(fw.rect_sum(0, 0, 1, 1) == 5);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
