"""Euler Angles and Rigid Body Kinematics.

Implements direction cosine matrix R(phi, theta, psi) and angular velocity transformation (Landau §35, Goldstein §4.4).
"""

from typing import Sequence
import numpy as np


class EulerAnglesKinematics:
    """Kinematics using Euler angles (phi, theta, psi) in Z-X-Z convention."""

    @staticmethod
    def rotation_matrix(phi: float, theta: float, psi: float) -> np.ndarray:
        """Direction cosine matrix R = R_z(psi) R_x(theta) R_z(phi)."""
        c1, s1 = np.cos(phi), np.sin(phi)
        c2, s2 = np.cos(theta), np.sin(theta)
        c3, s3 = np.cos(psi), np.sin(psi)

        return np.array([
            [c1 * c3 - s1 * c2 * s3,  s1 * c3 + c1 * c2 * s3, s2 * s3],
            [-c1 * s3 - s1 * c2 * c3, -s1 * s3 + c1 * c2 * c3, s2 * c3],
            [s1 * s2,                -c1 * s2,                c2]
        ], dtype=np.float64)

    @staticmethod
    def body_angular_velocity(phi: float, theta: float, psi: float,
                              phi_dot: float, theta_dot: float, psi_dot: float) -> np.ndarray:
        """Body frame angular velocity vector:
        w_1 = phi_dot sin(theta) sin(psi) + theta_dot cos(psi)
        w_2 = phi_dot sin(theta) cos(psi) - theta_dot sin(psi)
        w_3 = phi_dot cos(theta) + psi_dot
        """
        s_th, c_th = np.sin(theta), np.cos(theta)
        s_ps, c_ps = np.sin(psi), np.cos(psi)

        w1 = phi_dot * s_th * s_ps + theta_dot * c_ps
        w2 = phi_dot * s_th * c_ps - theta_dot * s_ps
        w3 = phi_dot * c_th + psi_dot
        return np.array([w1, w2, w3], dtype=np.float64)
