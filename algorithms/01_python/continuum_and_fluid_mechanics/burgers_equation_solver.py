"""
Viscous Burgers' Equation Solver via Upwind Finite Differences.
References: Kincaid & Cheney - Numerical Analysis.
"""
import numpy as np

def burgers_step_upwind(u: np.ndarray, dx: float, dt: float, nu: float = 0.01) -> np.ndarray:
    """Upwind advection + central difference diffusion for du/dt + u du/dx = nu d^2u/dx^2."""
    n = len(u)
    u_new = u.copy()
    for i in range(1, n - 1):
        # Upwind advection
        if u[i] >= 0:
            adv = u[i] * (u[i] - u[i - 1]) / dx
        else:
            adv = u[i] * (u[i + 1] - u[i]) / dx
        diff = nu * (u[i + 1] - 2 * u[i] + u[i - 1]) / (dx**2)
        u_new[i] = u[i] - dt * adv + dt * diff
    return u_new
