#ifndef RK4_INTEGRATOR_H
#define RK4_INTEGRATOR_H

typedef double (*ode_deriv_fn)(double t, double y);

double rk4_step(ode_deriv_fn f, double t, double y, double dt);

#endif
