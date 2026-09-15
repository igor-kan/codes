#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double bisection(const std::function<double(double)> &f, double a, double b) {
    double fa = f(a);
    for (int i = 0; i < 200; ++i) {
        double c = 0.5 * (a + b);
        double fc = f(c);
        if (fc == 0 || (b - a) / 2 < 1e-12) return c;
        if (fa * fc < 0) b = c; else { a = c; fa = fc; }
    }
    return 0.5 * (a + b);
}

int main() {
    assert(std::abs(bisection([](double x) { return x * x - 2; }, 0, 2) - std::sqrt(2.0)) < 1e-9);
    std::cout << "bisection ok\n";
    return 0;
}
