#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_two_sat_implication;
    TwoSatSolver s1(3);
    s1.add_xor(0, 1);
    s1.add_xor(1, 2);
    s1.force_true(0, false);
    auto r1 = s1.solve();
    assert(r1.satisfiable);
    assert(r1.assignment[0] && !r1.assignment[1] && r1.assignment[2]);

    TwoSatSolver s2(2);
    s2.add_xor(0, 1);
    s2.add_or(0, false, 1, false);
    s2.add_or(0, true, 1, true);
    s2.force_true(0, false);
    s2.force_true(1, false);
    assert(!s2.solve().satisfiable);
    return 0;
}
