"""Earthquake Focal Mechanism and Radiation Pattern."""

from typing import Tuple
import numpy as np


class FocalMechanism:
    """Strike, Dip, Rake conventions and double-couple P-wave radiation patterns."""

    @classmethod
    def fault_normal_and_slip(
        cls, strike_deg: float, dip_deg: float, rake_deg: float
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Calculates normal vector n and slip vector u in (North, East, Down) coordinates."""
        phi = np.radians(strike_deg)
        delta = np.radians(dip_deg)
        lam = np.radians(rake_deg)

        # Fault normal n pointing into hanging wall
        n = np.array([
            -np.sin(delta) * np.sin(phi),
            np.sin(delta) * np.cos(phi),
            -np.cos(delta)
        ])

        # Slip vector u
        u = np.array([
            np.cos(lam) * np.cos(phi) + np.cos(delta) * np.sin(lam) * np.sin(phi),
            np.cos(lam) * np.sin(phi) - np.cos(delta) * np.sin(lam) * np.cos(phi),
            -np.sin(delta) * np.sin(lam)
        ])

        return n, u

    @classmethod
    def p_wave_radiation_amplitude(cls, ray_vector: np.ndarray, normal: np.ndarray, slip: np.ndarray) -> float:
        """P-wave radiation pattern amplitude: A_P = (ray . normal) * (ray . slip)."""
        r = ray_vector / np.linalg.norm(ray_vector)
        return float(np.dot(r, normal) * np.dot(r, slip))
