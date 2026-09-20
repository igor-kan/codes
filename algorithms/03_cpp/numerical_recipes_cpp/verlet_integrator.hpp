#pragma once
#include <functional>
#include <vector>

namespace NumericalRecipes {

struct PhasePoint {
    double q;
    double p;
};

template <typename ForceFunc>
PhasePoint velocity_verlet_step(const PhasePoint& state, double dt, double mass, ForceFunc force) {
    double f = force(state.q);
    double p_half = state.p + 0.5 * dt * f;
    double q_new = state.q + dt * p_half / mass;
    double f_new = force(q_new);
    double p_new = p_half + 0.5 * dt * f_new;
    return {q_new, p_new};
}

} // namespace NumericalRecipes
