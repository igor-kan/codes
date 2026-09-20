"""
Symplectic Integrators: Verlet, Velocity Verlet, and Yoshida 4th Order.
References: Press et al. - Numerical Recipes (Ch. 17).
"""
import numpy as np

def velocity_verlet_step(q, p, force_func, m, dt):
    """Single Velocity Verlet step for H(q, p) = p^2/(2m) + V(q)."""
    f = force_func(q)
    p_half = p + 0.5 * dt * f
    q_new = q + dt * p_half / m
    f_new = force_func(q_new)
    p_new = p_half + 0.5 * dt * f_new
    return q_new, p_new

def yoshida4_step(q, p, force_func, m, dt):
    """Yoshida 4th-order symplectic integrator step."""
    theta = 1.0 / (2.0 - 2.0**(1.0 / 3.0))
    c1 = 0.5 * theta
    c4 = c1
    c2 = 0.5 * (1.0 - theta)
    c3 = c2

    d1 = theta
    d3 = d1
    d2 = 1.0 - 2.0 * theta
    d4 = 0.0

    # Sub-step 1
    q1 = q + c1 * dt * p / m
    p1 = p + d1 * dt * force_func(q1)
    # Sub-step 2
    q2 = q1 + c2 * dt * p1 / m
    p2 = p1 + d2 * dt * force_func(q2)
    # Sub-step 3
    q3 = q2 + c3 * dt * p2 / m
    p3 = p2 + d3 * dt * force_func(q3)
    # Sub-step 4
    q4 = q3 + c4 * dt * p3 / m
    p4 = p3
    return q4, p4
