"""Shooting Method with Secant Root-Finding for Two-Point BVP."""
import numpy as np
from scipy.integrate import solve_ivp


def shooting_linear_bvp(a: float, b: float, alpha: float, beta: float) -> float:
    """Solve y'' = y with y(a) = alpha, y(b) = beta."""
    def rhs(t, y):
        return [y[1], y[0]]
    
    # Shoot with slope s1 = 0, s2 = 1
    sol1 = solve_ivp(rhs, (a, b), [alpha, 0.0], t_eval=[b])
    sol2 = solve_ivp(rhs, (a, b), [alpha, 1.0], t_eval=[b])
    
    y_b1 = sol1.y[0, -1]
    y_b2 = sol2.y[0, -1]
    
    s_opt = (beta - y_b1) / (y_b2 - y_b1)
    return float(s_opt)
