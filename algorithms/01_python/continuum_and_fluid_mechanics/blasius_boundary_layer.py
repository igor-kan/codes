"""
Blasius Flat-Plate Boundary Layer Equation Solver.
Solves f''' + 0.5 f f'' = 0 with f(0) = f'(0) = 0, f'(inf) = 1.
References: Landau & Lifshitz - Fluid Mechanics (Vol. 6, Ch. 4).
"""
import numpy as np
from scipy.integrate import solve_ivp

def blasius_shooting(f_double_prime_0: float = 0.33206, eta_max: float = 8.0):
    """Integrate Blasius ODE using shooting method with given initial curvature f''(0)."""
    def odes(eta, y):
        # y = [f, f', f'']
        return [y[1], y[2], -0.5 * y[0] * y[2]]

    sol = solve_ivp(odes, (0.0, eta_max), [0.0, 0.0, f_double_prime_0], t_eval=np.linspace(0, eta_max, 200))
    return sol.t, sol.y
