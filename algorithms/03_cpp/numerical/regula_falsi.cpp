#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double regulaFalsi(const std::function<double(double)> &f, double a, double b) {
    double fa = f(a), fb = f(b), c = a;
    for (int i = 0; i < 200; ++i) {
        c = (a * fb - b * fa) / (fb - fa);
        double fc = f(c);
        if (std::abs(fc) < 1e-12) return c;
        if (fa * fc < 0) { b = c; fb = fc; } else { a = c; fa = fc; }
    }
    return c;
}

int main() {
    assert(std::abs(regulaFalsi([](double x) { return x * x - 2; }, 0, 2) - std::sqrt(2.0)) < 1e-9);
    std::cout << "regula falsi ok\n";
    return 0;
}
