"""Nonlinear Schrödinger Equation (NLSE) Solitons.

Equation: i * psi_t + (1/2) * psi_xx + g * |psi|^2 * psi = 0
"""

import numpy as np


class NLSESoliton:
    """Exact fundamental Bright (g > 0) and Dark (g < 0) solitons."""

    @classmethod
    def bright_soliton(
        cls, x: np.ndarray, t: float, amplitude: float = 1.0, velocity: float = 0.0, x0: float = 0.0
    ) -> np.ndarray:
        """Focusing NLSE (g = 1):
        psi(x, t) = eta * sech(eta * (x - v*t - x0)) * exp(i * (v*x - (v^2/2 - eta^2/2)*t))
        """
        eta = amplitude
        v = velocity
        xi = eta * (x - v * t - x0)
        envelope = eta / np.cosh(np.clip(xi, -50.0, 50.0))
        phase = v * x - (0.5 * (v**2) - 0.5 * (eta**2)) * t
        return envelope * np.exp(1j * phase)

    @classmethod
    def dark_soliton(
        cls, x: np.ndarray, t: float, background_density: float = 1.0, velocity: float = 0.0, x0: float = 0.0
    ) -> np.ndarray:
        """Defocusing NLSE (g = -1) black soliton (v=0):
        psi(x, t) = sqrt(rho_0) * tanh(sqrt(rho_0)*(x - x0)) * exp(-i * rho_0 * t)
        """
        rho0 = background_density
        k = np.sqrt(rho0)
        envelope = k * np.tanh(np.clip(k * (x - x0), -50.0, 50.0))
        phase = -rho0 * t
        return envelope * np.exp(1j * phase)
