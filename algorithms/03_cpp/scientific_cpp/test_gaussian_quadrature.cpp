#include <iostream>
#include <cassert>
#include <cmath>
#include "gaussian_quadrature.hpp"

int main() {
    // int_0^1 x^4 dx = 1/5 = 0.2 (exact for 3-point quadrature up to deg 5)
    double val = integrate_gauss_3point([](double x){ return x*x*x*x; }, 0.0, 1.0);
    assert(std::fabs(val - 0.2) < 1e-6);
    std::cout << "test_gaussian_quadrature PASSED\n";
    return 0;
}
