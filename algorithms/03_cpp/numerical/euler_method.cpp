#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double eulerMethod(const std::function<double(double, double)> &f, double y, double t, double t1, int steps) {
    double h = (t1 - t) / steps;
    for (int i = 0; i < steps; ++i) { y += h * f(t, y); t += h; }
    return y;
}

int main() {
    assert(std::abs(eulerMethod([](double, double y) { return y; }, 1.0, 0.0, 1.0, 1000) - std::exp(1.0)) < 0.01);
    std::cout << "euler method ok\n";
    return 0;
}
