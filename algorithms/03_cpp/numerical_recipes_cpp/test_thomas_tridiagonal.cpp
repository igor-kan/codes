#include "thomas_tridiagonal.hpp"
#include <cassert>
#include <cmath>
#include <iostream>

int main() {
    std::vector<double> b{4.0, 4.0, 4.0, 4.0};
    std::vector<double> a{1.0, 1.0, 1.0};
    std::vector<double> c{1.0, 1.0, 1.0};
    std::vector<double> d{5.0, 6.0, 6.0, 5.0};
    auto x = NumericalRecipes::solve_tridiagonal(a, b, c, d);
    for (double val : x) {
        assert(std::abs(val - 1.0) < 1e-10);
    }
    std::cout << "test_thomas_tridiagonal passed\n";
    return 0;
}
