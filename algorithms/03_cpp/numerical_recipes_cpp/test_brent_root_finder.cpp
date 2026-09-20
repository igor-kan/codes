#include "brent_root_finder.hpp"
#include <cassert>
#include <cmath>
#include <iostream>

int main() {
    auto f = [](double x) { return x * x * x - 2.0 * x - 5.0; };
    double root = NumericalRecipes::brent_find_root(f, 2.0, 3.0);
    assert(std::abs(f(root)) < 1e-7);
    std::cout << "test_brent_root_finder passed\n";
    return 0;
}
