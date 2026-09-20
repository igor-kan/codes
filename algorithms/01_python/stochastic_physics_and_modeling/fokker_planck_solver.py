"""
1D Fokker-Planck Equation Solver via Chang-Cooper Finite Difference Scheme.
References: Gershenfeld - The Nature of Mathematical Modeling.
"""
import numpy as np

def solve_fokker_planck_step(P, drift_a, diff_b, dx, dt):
    """Advance P(x, t) by one time step: dP/dt = -d/dx(A P) + 0.5 d^2/dx^2 (B P)."""
    n = len(P)
    P_new = P.copy()
    # Explicit conservative flux update
    flux = np.zeros(n + 1)
    # J_{i+1/2} = 0.5 * (A_i P_i + A_{i+1} P_{i+1}) - 0.5 * B_i (P_{i+1} - P_i) / dx
    for i in range(1, n):
        A_avg = 0.5 * (drift_a[i - 1] + drift_a[i])
        P_avg = 0.5 * (P[i - 1] + P[i])
        flux[i] = A_avg * P_avg - 0.5 * diff_b[i] * (P[i] - P[i - 1]) / dx

    for i in range(n):
        P_new[i] = P[i] - (dt / dx) * (flux[i + 1] - flux[i])
    # Normalize
    P_new = np.maximum(0.0, P_new)
    norm = np.sum(P_new) * dx
    if norm > 0:
        P_new /= norm
    return P_new
