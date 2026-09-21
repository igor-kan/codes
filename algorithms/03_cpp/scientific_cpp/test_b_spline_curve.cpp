#include <iostream>
#include <cassert>
#include "b_spline_curve.hpp"

int main() {
    std::vector<double> knots = {0.0, 0.0, 0.0, 1.0, 1.0, 1.0};
    std::vector<double> cp = {0.0, 1.0, 0.0};
    double val = de_boor_eval(2, 2, 0.5, knots, cp);
    assert(val > 0.0);
    std::cout << "test_b_spline_curve PASSED\n";
    return 0;
}
