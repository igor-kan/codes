#include <iostream>
#include <cassert>
#include <cmath>
#include "cholesky_decomposition.hpp"

int main() {
    std::vector<std::vector<double>> A = {
        {4.0, 12.0, -16.0},
        {12.0, 37.0, -43.0},
        {-16.0, -43.0, 98.0}
    };
    std::vector<std::vector<double>> L;
    bool ok = cholesky_factorize(A, L);
    assert(ok);
    assert(std::fabs(L[0][0] - 2.0) < 1e-6);
    assert(std::fabs(L[1][0] - 6.0) < 1e-6);
    std::cout << "test_cholesky_decomposition PASSED\n";
    return 0;
}
