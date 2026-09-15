#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

std::pair<double, double> verlet(const std::function<double(double)> &acceleration, double x, double v,
                                 double dt, int steps) {
    for (int i = 0; i < steps; ++i) {
        double a = acceleration(x);
        double xNew = x + v * dt + 0.5 * a * dt * dt;
        double aNew = acceleration(xNew);
        v = v + 0.5 * (a + aNew) * dt;
        x = xNew;
    }
    return {x, v};
}

int main() {
    auto [position, velocity] = verlet([](double x) { return -x; }, 1.0, 0.0, 0.001, 10000);
    double energy = 0.5 * (velocity * velocity + position * position);
    assert(std::abs(energy - 0.5) < 1e-3);
    assert(std::abs(position - std::cos(10.0)) < 1e-2);
    std::cout << "verlet ok\n";
    return 0;
}
