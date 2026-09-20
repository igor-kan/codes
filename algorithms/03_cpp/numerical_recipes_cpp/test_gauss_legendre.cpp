#include "gauss_legendre.hpp"
#include <cassert>
#include <cmath>
#include <iostream>

int main() {
    // int_0^1 x^4 dx = 1/5 = 0.2
    auto f = [](double x) { return x * x * x * x; };
    double val = NumericalRecipes::integrate_gauss_legendre_3pt(f, 0.0, 1.0);
    assert(std::abs(val - 0.2) < 1e-10);
    std::cout << "test_gauss_legendre passed\n";
    return 0;
}
