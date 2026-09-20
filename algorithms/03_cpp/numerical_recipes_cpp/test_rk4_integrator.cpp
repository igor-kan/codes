#include "rk4_integrator.hpp"
#include <cassert>
#include <cmath>
#include <iostream>

int main() {
    using State = std::vector<double>;
    auto derivs = [](double t, const State& y) {
        return State{-y[0]};
    };
    State y{1.0};
    double dt = 0.01;
    for (int step = 0; step < 100; ++step) {
        y = NumericalRecipes::rk4_step(y, step * dt, dt, derivs);
    }
    assert(std::abs(y[0] - std::exp(-1.0)) < 1e-6);
    std::cout << "test_rk4_integrator passed\n";
    return 0;
}
