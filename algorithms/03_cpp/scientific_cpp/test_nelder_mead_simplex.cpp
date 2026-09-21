#include <iostream>
#include <cassert>
#include <cmath>
#include "nelder_mead_simplex.hpp"

int main() {
    // Paraboloid: f(x, y) = (x - 3)^2 + (y - 5)^2
    auto f = [](const std::vector<double>& v) {
        return (v[0] - 3.0)*(v[0] - 3.0) + (v[1] - 5.0)*(v[1] - 5.0);
    };
    auto x_min = nelder_mead_minimize(f, {0.0, 0.0}, 1.0, 200);
    assert(std::fabs(x_min[0] - 3.0) < 0.1);
    assert(std::fabs(x_min[1] - 5.0) < 0.1);
    std::cout << "test_nelder_mead_simplex PASSED\n";
    return 0;
}
