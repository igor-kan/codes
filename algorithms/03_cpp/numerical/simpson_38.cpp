// Composite Simpson's 3/8 rule (Numerical Recipes 4.1).
#include <cassert>
#include <functional>
#include <iostream>

double simpson38(const std::function<double(double)> &f, double a, double b, int n) {
    if (n % 3) n += 3 - n % 3;
    double h = (b - a) / n, total = f(a) + f(b);
    for (int i = 1; i < n; ++i) total += (i % 3 ? 3.0 : 2.0) * f(a + i * h);
    return 3.0 * h / 8.0 * total;
}

int main() {
    assert(std::abs(simpson38([](double x) { return x * x; }, 0, 1, 999) - 1.0 / 3.0) < 1e-12);
    std::cout << "simpson 3/8 ok\n";
    return 0;
}
