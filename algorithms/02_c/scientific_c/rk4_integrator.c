#include "rk4_integrator.h"

double rk4_step(ode_deriv_fn f, double t, double y, double dt) {
    double k1 = f(t, y);
    double k2 = f(t + 0.5 * dt, y + 0.5 * dt * k1);
    double k3 = f(t + 0.5 * dt, y + 0.5 * dt * k2);
    double k4 = f(t + dt, y + dt * k3);
    return y + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4);
}
