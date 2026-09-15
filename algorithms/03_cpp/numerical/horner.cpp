// Horner's method (Numerical Recipes 5.3).
#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

std::pair<double, double> hornerWithDerivative(const std::vector<double> &c, double x) {
    double value = 0.0, derivative = 0.0;
    for (auto it = c.rbegin(); it != c.rend(); ++it) {
        derivative = derivative * x + value;
        value = value * x + *it;
    }
    return {value, derivative};
}

int main() {
    std::vector<double> c{-1.0, 2.0, -6.0, 2.0};
    auto [value, derivative] = hornerWithDerivative(c, 3.0);
    assert(std::abs(value - 5.0) < 1e-9 && std::abs(derivative - 20.0) < 1e-9);
    std::cout << "horner ok\n";
    return 0;
}
