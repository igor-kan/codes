"""Hamilton-Jacobi Equation and Characteristic Function W(q, alpha).

Implements Landau & Lifshitz §47 and Arnold §46: H(q, dW/dq) = E with separation of variables.
"""

from typing import Callable, Sequence
import numpy as np


class HamiltonJacobiSolver:
    """Hamilton-Jacobi separation of variables for conservative systems."""

    def __init__(self, energy: float):
        self.energy = energy

    def characteristic_momentum_1d(self, potential_func: Callable[[float], float],
                                   mass: float, q: float) -> float:
        """dW/dq = sqrt(2 m (E - V(q)))."""
        kinetic = 2.0 * mass * (self.energy - potential_func(q))
        if kinetic < 0.0:
            raise ValueError(f"Classical turning point reached at q={q}: E < V(q)")
        return float(np.sqrt(kinetic))

    def action_integral_1d(self, potential_func: Callable[[float], float],
                           mass: float, q1: float, q2: float, num_points: int = 1000) -> float:
        """W = int_{q1}^{q2} sqrt(2 m (E - V(q))) dq."""
        q_vals = np.linspace(q1, q2, num_points)
        dq = (q2 - q1) / (num_points - 1)
        integrand = [self.characteristic_momentum_1d(potential_func, mass, q) for q in q_vals]
        return float(np.trapezoid(integrand, dx=dq))
