"""Non-Holonomic Velocity Constraints and D'Alembert-Lagrange Equations.

Implements Pfaffian non-integrable velocity constraints A(q) dot{q} = 0 using Lagrange multipliers.
"""

from typing import Sequence
import numpy as np


class NonHolonomicSystem:
    """Solves constrained equations: M dot{v} = F_applied + A^T lambda subject to A dot{q} = 0."""

    def __init__(self, mass_matrix: Sequence[Sequence[float]]):
        self.m = np.array(mass_matrix, dtype=np.float64)
        self.inv_m = np.linalg.inv(self.m)
        self.dim = self.m.shape[0]

    def constrained_acceleration(self, applied_forces: Sequence[float],
                                 constraint_matrix: Sequence[Sequence[float]],
                                 constraint_drift: Sequence[float]) -> np.ndarray:
        """Solve for acceleration dot{v} and multipliers lambda:
        A dot{v} = - constraint_drift
        lambda = (A M^{-1} A^T)^{-1} (- constraint_drift - A M^{-1} F)
        """
        f = np.array(applied_forces, dtype=np.float64)
        a = np.array(constraint_matrix, dtype=np.float64)
        drift = np.array(constraint_drift, dtype=np.float64)

        # Gram matrix G = A M^{-1} A^T
        gram = a @ self.inv_m @ a.T
        rhs = - drift - a @ self.inv_m @ f
        lambdas = np.linalg.solve(gram, rhs)

        # Acceleration dot{v} = M^{-1} (F + A^T lambda)
        f_constraint = a.T @ lambdas
        q_ddot = self.inv_m @ (f + f_constraint)
        return q_ddot
