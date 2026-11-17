#include "interface.hpp"
#include <cassert>

int main() {
    using namespace codes_gaussian_xor_basis;
    XorBasis b1, b2;
    for (std::uint64_t x : {12ULL, 18ULL, 25ULL}) b1.insert(x);
    for (std::uint64_t x : {31ULL, 4ULL, 19ULL}) b2.insert(x);
    b1.merge(b2);
    verify_xor_basis_invariants(b1);
    auto out = parallel_basis_max_queries({12ULL, 18ULL, 25ULL, 31ULL}, {0ULL, 1ULL, 7ULL});
    assert(out[0] == 31ULL);
    return 0;
}
