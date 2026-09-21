#include <iostream>
#include <cassert>
#include <cmath>
#include "rk45_dormand_prince.hpp"

int main() {
    double y = 1.0;
    double t = 0.0;
    double h = 0.1;
    // dy/dt = y -> y(0.1) = exp(0.1)
    y = dormand_prince_step([](double t, double y){ (void)t; return y; }, t, y, h);
    assert(std::fabs(y - std::exp(0.1)) < 1e-6);
    std::cout << "test_rk45_dormand_prince PASSED\n";
    return 0;
}
