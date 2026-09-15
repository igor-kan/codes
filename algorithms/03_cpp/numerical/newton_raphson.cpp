// Newton-Raphson root finding (Numerical Recipes 9.4).
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>

double newton(const std::function<double(double)> &f,
              const std::function<double(double)> &df, double x) {
    for (int i = 0; i < 100; ++i) {
        double fx = f(x);
        if (std::abs(fx) < 1e-12) break;
        x -= fx / df(x);
    }
    return x;
}

int main() {
    double root = newton([](double x) { return x * x - 2; }, [](double x) { return 2 * x; }, 1.0);
    assert(std::abs(root - std::sqrt(2.0)) < 1e-9);
    std::cout << "newton-raphson ok\n";
    return 0;
}
