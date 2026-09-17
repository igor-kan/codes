"""Euler Dynamical Equations for Rigid Body Rotation and the Tennis Racket Theorem.

Implements Landau & Lifshitz §36 and Goldstein §5.6:
I_1 dot{omega}_1 - (I_2 - I_3) omega_2 omega_3 = N_1.
Demonstrates the intermediate axis instability (Dzhanibekov effect).
"""

from typing import Sequence, Tuple
import numpy as np


class EulerRigidBody:
    """Euler dynamical equations of motion for an asymmetric top."""

    def __init__(self, principal_moments: Sequence[float]):
        self.i1, self.i2, self.i3 = principal_moments
        if self.i1 <= 0 or self.i2 <= 0 or self.i3 <= 0:
            raise ValueError("Principal moments of inertia must be strictly positive")

    def time_derivatives(self, omega: Sequence[float], external_torque: Sequence[float] = (0.0, 0.0, 0.0)) -> np.ndarray:
        """Compute (dot{omega}_1, dot{omega}_2, dot{omega}_3)."""
        w1, w2, w3 = omega
        n1, n2, n3 = external_torque
        dw1 = (n1 + (self.i2 - self.i3) * w2 * w3) / self.i1
        dw2 = (n2 + (self.i3 - self.i1) * w3 * w1) / self.i2
        dw3 = (n3 + (self.i1 - self.i2) * w1 * w2) / self.i3
        return np.array([dw1, dw2, dw3], dtype=np.float64)

    def intermediate_axis_instability_eigenvalues(self, w0: float) -> Tuple[complex, complex]:
        """Linearized perturbations around intermediate axis 2 (assuming I_1 < I_2 < I_3) give real positive eigenvalues (hyperbolic saddle / instability)."""
        factor = ((self.i3 - self.i2) * (self.i2 - self.i1) / (self.i1 * self.i3)) * (w0**2)
        lam = np.sqrt(factor + 0j)
        return lam, -lam
