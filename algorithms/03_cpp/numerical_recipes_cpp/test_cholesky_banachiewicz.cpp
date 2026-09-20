#include "cholesky_banachiewicz.hpp"
#include <cassert>
#include <cmath>
#include <iostream>

int main() {
    std::vector<std::vector<double>> A = {
        {4.0, 12.0, -16.0},
        {12.0, 37.0, -43.0},
        {-16.0, -43.0, 98.0}
    };
    auto L = NumericalRecipes::cholesky_decompose(A);
    assert(std::abs(L[0][0] - 2.0) < 1e-10);
    assert(std::abs(L[1][0] - 6.0) < 1e-10);
    assert(std::abs(L[1][1] - 1.0) < 1e-10);
    assert(std::abs(L[2][0] - (-8.0)) < 1e-10);
    assert(std::abs(L[2][1] - 5.0) < 1e-10);
    assert(std::abs(L[2][2] - 3.0) < 1e-10);
    std::cout << "test_cholesky_banachiewicz passed\n";
    return 0;
}
