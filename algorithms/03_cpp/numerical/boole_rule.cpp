// Composite Boole's rule (Numerical Recipes 4.1).
#include <cassert>
#include <functional>
#include <iostream>

double booleRule(const std::function<double(double)> &f, double a, double b, int n) {
    if (n % 4) n += 4 - n % 4;
    double h = (b - a) / n, total = 7.0 * (f(a) + f(b));
    for (int i = 1; i < n; ++i) {
        if (i % 4 == 0) total += 14.0 * f(a + i * h);
        else if (i % 2 == 0) total += 12.0 * f(a + i * h);
        else total += 32.0 * f(a + i * h);
    }
    return 2.0 * h / 45.0 * total;
}

int main() {
    assert(std::abs(booleRule([](double x) { return x * x; }, 0, 1, 998) - 1.0 / 3.0) < 1e-12);
    std::cout << "boole rule ok\n";
    return 0;
}
