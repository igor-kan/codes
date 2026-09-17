"""Sine-Gordon equation topological solitons (kinks, anti-kinks) and breathers.

Equation: phi_tt - phi_xx + sin(phi) = 0
"""

import numpy as np


class SineGordonSoliton:
    """Exact topological and non-topological solutions to Sine-Gordon equation."""

    @classmethod
    def kink(cls, x: np.ndarray, t: float, v: float = 0.0, x0: float = 0.0) -> np.ndarray:
        """Topological kink: phi(x, t) = 4 * arctan(exp(gamma * (x - v*t - x0)))
        where gamma = 1 / sqrt(1 - v^2).
        """
        gamma = 1.0 / np.sqrt(1.0 - v**2)
        arg = np.clip(gamma * (x - v * t - x0), -50.0, 50.0)
        return 4.0 * np.arctan(np.exp(arg))

    @classmethod
    def anti_kink(cls, x: np.ndarray, t: float, v: float = 0.0, x0: float = 0.0) -> np.ndarray:
        """Anti-kink: phi(x, t) = 4 * arctan(exp(-gamma * (x - v*t - x0)))."""
        gamma = 1.0 / np.sqrt(1.0 - v**2)
        arg = np.clip(-gamma * (x - v * t - x0), -50.0, 50.0)
        return 4.0 * np.arctan(np.exp(arg))

    @classmethod
    def breather(cls, x: np.ndarray, t: float, omega: float = 0.5) -> np.ndarray:
        """Breather oscillating bound state for omega in (0, 1):
        phi(x, t) = -4 * arctan( (sqrt(1-omega^2)/omega) * (sin(omega*t) / cosh(sqrt(1-omega^2)*x)) )
        """
        eta = np.sqrt(1.0 - omega**2)
        arg = (eta / omega) * (np.sin(omega * t) / np.cosh(np.clip(eta * x, -50.0, 50.0)))
        return -4.0 * np.arctan(arg)
