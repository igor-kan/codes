#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double fixedPoint(const std::function<double(double)> &g, double x) {
    for (int i = 0; i < 200; ++i) {
        double next = g(x);
        if (std::abs(next - x) < 1e-12) return next;
        x = next;
    }
    return x;
}

int main() {
    assert(std::abs(fixedPoint([](double x) { return 0.5 * (x + 2 / x); }, 1.0) - std::sqrt(2.0)) < 1e-9);
    std::cout << "fixed point ok\n";
    return 0;
}
