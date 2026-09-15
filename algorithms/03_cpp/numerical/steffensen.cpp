#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double steffensen(const std::function<double(double)> &g, double x) {
    for (int i = 0; i < 100; ++i) {
        double x1 = g(x), x2 = g(x1);
        double denominator = x2 - 2 * x1 + x;
        if (std::abs(denominator) < 1e-15) return x2;
        double next = x - (x1 - x) * (x1 - x) / denominator;
        if (std::abs(next - x) < 1e-12) return next;
        x = next;
    }
    return x;
}

int main() {
    assert(std::abs(steffensen([](double x) { return 0.5 * (x + 2 / x); }, 1.0) - std::sqrt(2.0)) < 1e-12);
    std::cout << "steffensen ok\n";
    return 0;
}
