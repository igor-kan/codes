#include <iostream>
#include <cassert>
#include <cmath>
#include "qr_eigenvalues.hpp"

int main() {
    auto eigs = compute_symmetric_eigenvalues_2x2(2.0, 1.0, 2.0);
    // (2-l)^2 - 1 = 0 -> l = 1, 3
    assert(std::fabs(eigs[0] - 1.0) < 1e-6);
    assert(std::fabs(eigs[1] - 3.0) < 1e-6);
    std::cout << "test_qr_eigenvalues PASSED\n";
    return 0;
}
