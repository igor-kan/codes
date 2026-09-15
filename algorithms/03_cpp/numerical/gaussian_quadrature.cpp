// Gauss-Legendre quadrature (Numerical Recipes 4.5).
#include <cassert>
#include <functional>
#include <iostream>

double gaussianQuadrature(const std::function<double(double)> &f, double a, double b) {
    const double nodes[] = {0.0, -0.5384693101056831, 0.5384693101056831,
                            -0.9061798459386640, 0.9061798459386640};
    const double weights[] = {0.5688888888888889, 0.4786286704993665, 0.4786286704993665,
                              0.2369268850561891, 0.2369268850561891};
    double midpoint = 0.5 * (a + b), half = 0.5 * (b - a), total = 0.0;
    for (int i = 0; i < 5; ++i) total += weights[i] * f(midpoint + half * nodes[i]);
    return total * half;
}

int main() {
    assert(std::abs(gaussianQuadrature([](double x) { return x * x; }, 0, 1) - 1.0 / 3.0) < 1e-12);
    assert(std::abs(gaussianQuadrature([](double x) { return x * x * x * x * x * x * x; }, 0, 1) - 1.0 / 8.0) < 1e-12);
    std::cout << "gaussian quadrature ok\n";
    return 0;
}
