#include <iostream>
#include <cassert>
#include <cmath>
#include "spline_interpolation.hpp"

int main() {
    std::vector<double> x = {0.0, 1.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    CubicSpline cs(x, y);
    // Interpolates points exactly
    assert(std::fabs(cs.eval(0.0) - 0.0) < 1e-6);
    assert(std::fabs(cs.eval(1.0) - 1.0) < 1e-6);
    assert(std::fabs(cs.eval(2.0) - 4.0) < 1e-6);
    std::cout << "test_spline_interpolation PASSED\n";
    return 0;
}
