// Composite Simpson's rule (Numerical Recipes 4.1).
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>

double simpson(const std::function<double(double)> &f, double a, double b, int n = 1000) {
    if (n % 2) ++n;
    double h = (b - a) / n;
    double total = f(a) + f(b);
    for (int i = 1; i < n; ++i) total += (i % 2 ? 4.0 : 2.0) * f(a + i * h);
    return total * h / 3.0;
}

int main() {
    assert(std::abs(simpson([](double x) { return x * x; }, 0, 1) - 1.0 / 3) < 1e-12);
    std::cout << "simpson integration ok\n";
    return 0;
}
