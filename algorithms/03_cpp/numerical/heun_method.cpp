#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double heunMethod(const std::function<double(double, double)> &f, double y, double t, double t1, int steps) {
    double h = (t1 - t) / steps;
    for (int i = 0; i < steps; ++i) {
        double k1 = f(t, y);
        double k2 = f(t + h, y + h * k1);
        y += 0.5 * h * (k1 + k2);
        t += h;
    }
    return y;
}

int main() {
    assert(std::abs(heunMethod([](double, double y) { return y; }, 1.0, 0.0, 1.0, 1000) - std::exp(1.0)) < 1e-4);
    std::cout << "heun method ok\n";
    return 0;
}
