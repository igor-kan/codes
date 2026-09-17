"""Lane-Emden Equation for polytropic stellar structure.

Solves the dimensionless hydrostatic equation:
(1/xi^2) d/dxi (xi^2 dtheta/dxi) = -theta^n
using Runge-Kutta 4th order integration.
"""

from typing import Tuple, List
import numpy as np


class LaneEmdenSolver:
    """Numerical solver for the Lane-Emden polytrope equation of index n."""

    def __init__(self, n: float, dxi: float = 1e-4, xi_max: float = 40.0):
        self.n = float(n)
        self.dxi = float(dxi)
        self.xi_max = float(xi_max)

    def solve(self) -> Tuple[np.ndarray, np.ndarray, float, float]:
        """Integrates outward from center (xi=0) to stellar surface (theta=0).

        Returns:
            (xi_array, theta_array, xi_surface, dtheta_dxi_surface)
        """
        xi = 1e-5
        # Taylor expansion near center: theta = 1 - xi^2/6 + (n/120)*xi^4
        theta = 1.0 - (xi**2) / 6.0
        dtheta = -xi / 3.0

        xi_vals = [0.0, xi]
        theta_vals = [1.0, theta]

        while xi < self.xi_max and theta > 0:
            # RK4 step for system:
            # y0 = theta, y1 = dtheta/dxi
            # dy0/dxi = y1
            # dy1/dxi = - (2/xi)*y1 - theta^n (if theta > 0 else 0)
            def deriv(x: float, y: np.ndarray) -> np.ndarray:
                th, dth = y[0], y[1]
                th_term = (th**self.n) if th > 0 else 0.0
                return np.array([dth, -(2.0 / x) * dth - th_term])

            y = np.array([theta, dtheta])
            h = self.dxi

            k1 = deriv(xi, y)
            k2 = deriv(xi + 0.5 * h, y + 0.5 * h * k1)
            k3 = deriv(xi + 0.5 * h, y + 0.5 * h * k2)
            k4 = deriv(xi + h, y + h * k3)

            y_next = y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

            xi += h
            theta = y_next[0]
            dtheta = y_next[1]

            if theta >= 0:
                xi_vals.append(xi)
                theta_vals.append(theta)
            else:
                # Linear interpolation for zero crossing
                fraction = theta_vals[-1] / (theta_vals[-1] - theta)
                xi_surf = xi_vals[-1] + fraction * h
                dtheta_surf = dtheta
                return np.array(xi_vals), np.array(theta_vals), xi_surf, dtheta_surf

        return np.array(xi_vals), np.array(theta_vals), xi, dtheta
