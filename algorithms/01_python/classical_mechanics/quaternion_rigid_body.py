"""Unit Quaternions (Euler-Rodrigues Parameters) for Singularity-Free Attitude Kinematics.

Solves the gimbal lock problem via S^3 Spin(3) kinematics: dot{q} = 1/2 q * omega.
"""

from typing import Sequence
import numpy as np


class QuaternionRigidBody:
    """Unit quaternion q = (q0, q1, q2, q3) attitude representation."""

    def __init__(self, q: Sequence[float]):
        self.q = np.array(q, dtype=np.float64)
        norm = np.linalg.norm(self.q)
        if norm < 1e-12:
            raise ValueError("Quaternion cannot have zero norm")
        self.q = self.q / norm

    def to_rotation_matrix(self) -> np.ndarray:
        """Convert quaternion to 3x3 orthogonal rotation matrix R(q) in SO(3)."""
        q0, q1, q2, q3 = self.q
        return np.array([
            [1.0 - 2.0 * (q2**2 + q3**2), 2.0 * (q1 * q2 - q0 * q3), 2.0 * (q1 * q3 + q0 * q2)],
            [2.0 * (q1 * q2 + q0 * q3), 1.0 - 2.0 * (q1**2 + q3**2), 2.0 * (q2 * q3 - q0 * q1)],
            [2.0 * (q1 * q3 - q0 * q2), 2.0 * (q2 * q3 + q0 * q1), 1.0 - 2.0 * (q1**2 + q2**2)]
        ], dtype=np.float64)

    def kinematic_derivative(self, body_omega: Sequence[float]) -> np.ndarray:
        """dot{q} = 1/2 W * q where W is skew-symmetric angular velocity matrix."""
        w1, w2, w3 = body_omega
        omega_mat = np.array([
            [0.0, -w1, -w2, -w3],
            [w1,  0.0,  w3, -w2],
            [w2, -w3,  0.0,  w1],
            [w3,  w2, -w1,  0.0]
        ], dtype=np.float64)
        return 0.5 * (omega_mat @ self.q)
