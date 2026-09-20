#pragma once
#include <functional>
#include <vector>

namespace NumericalRecipes {

template <typename State, typename DerivFunc>
State rk4_step(const State& y, double t, double dt, DerivFunc derivs) {
    State k1 = derivs(t, y);
    State y_k1 = y;
    for (size_t i = 0; i < y.size(); ++i) y_k1[i] += 0.5 * dt * k1[i];
    State k2 = derivs(t + 0.5 * dt, y_k1);
    State y_k2 = y;
    for (size_t i = 0; i < y.size(); ++i) y_k2[i] += 0.5 * dt * k2[i];
    State k3 = derivs(t + 0.5 * dt, y_k2);
    State y_k3 = y;
    for (size_t i = 0; i < y.size(); ++i) y_k3[i] += dt * k3[i];
    State k4 = derivs(t + dt, y_k3);

    State y_next = y;
    for (size_t i = 0; i < y.size(); ++i) {
        y_next[i] += (dt / 6.0) * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]);
    }
    return y_next;
}

} // namespace NumericalRecipes
