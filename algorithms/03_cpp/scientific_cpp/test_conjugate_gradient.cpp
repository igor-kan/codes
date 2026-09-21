#include <iostream>
#include <cassert>
#include <cmath>
#include "conjugate_gradient.hpp"

int main() {
    std::vector<std::vector<double>> A = {
        {4.0, 1.0},
        {1.0, 3.0}
    };
    std::vector<double> b = {1.0, 2.0};
    auto x = solve_cg(A, b);
    // 4x + y = 1, x + 3y = 2 -> 11x = 1 -> x = 1/11, y = 7/11
    assert(std::fabs(x[0] - 1.0/11.0) < 1e-5);
    assert(std::fabs(x[1] - 7.0/11.0) < 1e-5);
    std::cout << "test_conjugate_gradient PASSED\n";
    return 0;
}
