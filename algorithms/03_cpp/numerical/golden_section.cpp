// Golden-section search for a 1D minimum (Numerical Recipes 10.1).
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>

double goldenSection(const std::function<double(double)> &f, double a, double b) {
    const double invPhi = (std::sqrt(5.0) - 1) / 2;
    double c = b - invPhi * (b - a), d = a + invPhi * (b - a);
    double fc = f(c), fd = f(d);
    while (b - a > 1e-9) {
        if (fc < fd) { b = d; d = c; fd = fc; c = b - invPhi * (b - a); fc = f(c); }
        else { a = c; c = d; fc = fd; d = a + invPhi * (b - a); fd = f(d); }
    }
    return (a + b) / 2;
}

int main() {
    double x = goldenSection([](double x) { return (x - 3) * (x - 3); }, -10, 10);
    assert(std::abs(x - 3) < 1e-6);
    std::cout << "golden section ok\n";
    return 0;
}
