#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_gaussian_xor_basis;
    XorBasis b;
    b.insert(3);
    b.insert(5);
    assert(b.insert(3 ^ 5) == false);
    assert(b.rank() == 2);
    assert(b.max_xor() == 6);
    assert(b.kth_smallest(0) == 0);
    assert(b.kth_smallest(1) == 3);
    assert(b.kth_smallest(2) == 5);
    assert(b.kth_smallest(3) == 6);
    assert(b.can_represent(6));
    assert(!b.can_represent(7));
    verify_xor_basis_invariants(b);
    return 0;
}
