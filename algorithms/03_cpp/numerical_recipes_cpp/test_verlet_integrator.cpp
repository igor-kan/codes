#include "verlet_integrator.hpp"
#include <cassert>
#include <cmath>
#include <iostream>

int main() {
    NumericalRecipes::PhasePoint state{1.0, 0.0};
    auto force = [](double q) { return -q; };
    for (int i = 0; i < 100; ++i) {
        state = NumericalRecipes::velocity_verlet_step(state, 0.05, 1.0, force);
    }
    double E = 0.5 * (state.p * state.p + state.q * state.q);
    assert(std::abs(E - 0.5) < 1e-3);
    std::cout << "test_verlet_integrator passed\n";
    return 0;
}
