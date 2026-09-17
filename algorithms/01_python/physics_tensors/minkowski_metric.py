"""Minkowski Spacetime Metric eta_{mu nu} and Lorentz Boost Tensors.

Implements flat spacetime geometry, 4-vectors, Lorentz boosts, and spatial rotations.
"""

from typing import Sequence
import numpy as np
try:
    from .metric_tensor import MetricTensor
except ImportError:
    from metric_tensor import MetricTensor


class MinkowskiSpacetime:
    """Minkowski flat spacetime with signature (-, +, +, +)."""

    C = 299792458.0  # Speed of light in m/s

    def __init__(self, c: float = 1.0):
        self.c = c
        self.eta = MetricTensor(np.diag([-1.0, 1.0, 1.0, 1.0]))

    def lorentz_boost(self, beta: Sequence[float]) -> np.ndarray:
        """Compute Lorentz transformation matrix Lambda^mu_nu for velocity vector beta = v/c."""
        bx, by, bz = beta
        b2 = bx**2 + by**2 + bz**2
        if b2 >= 1.0:
            raise ValueError(f"Beta magnitude {np.sqrt(b2)} must be strictly less than 1")
        if b2 < 1e-15:
            return np.eye(4)

        gamma = 1.0 / np.sqrt(1.0 - b2)
        b = np.sqrt(b2)
        nx, ny, nz = bx / b, by / b, bz / b

        lambda_matrix = np.eye(4)
        lambda_matrix[0, 0] = gamma
        lambda_matrix[0, 1:] = -gamma * np.array([bx, by, bz])
        lambda_matrix[1:, 0] = -gamma * np.array([bx, by, bz])

        outer_n = np.outer([nx, ny, nz], [nx, ny, nz])
        lambda_matrix[1:, 1:] = np.eye(3) + (gamma - 1.0) * outer_n
        return lambda_matrix

    def four_velocity(self, v_3d: Sequence[float]) -> np.ndarray:
        """Compute four-velocity u^mu = gamma * (c, v_x, v_y, v_z)."""
        v = np.array(v_3d, dtype=np.float64)
        v2 = np.sum(v**2)
        beta2 = v2 / (self.c**2)
        if beta2 >= 1.0:
            raise ValueError("Velocity must be less than c")
        gamma = 1.0 / np.sqrt(1.0 - beta2)
        return gamma * np.array([self.c, v[0], v[1], v[2]])

    def invariant_norm_sq(self, four_vector: Sequence[float]) -> float:
        """Returns eta_{mu nu} u^mu u^nu."""
        return self.eta.line_element(four_vector)
