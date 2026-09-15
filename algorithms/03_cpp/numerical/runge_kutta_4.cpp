// Classical fourth-order Runge-Kutta (Numerical Recipes 17.1).
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>

double rk4(const std::function<double(double, double)> &f, double y,
           double t0, double t1, int steps = 1000) {
    double h = (t1 - t0) / steps;
    double t = t0;
    for (int i = 0; i < steps; ++i) {
        double k1 = h * f(t, y);
        double k2 = h * f(t + h / 2, y + k1 / 2);
        double k3 = h * f(t + h / 2, y + k2 / 2);
        double k4 = h * f(t + h, y + k3);
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6;
        t += h;
    }
    return y;
}

int main() {
    double value = rk4([](double, double y) { return y; }, 1.0, 0.0, 1.0);
    assert(std::abs(value - std::exp(1.0)) < 1e-9);
    std::cout << "runge-kutta 4 ok\n";
    return 0;
}
