"""Anharmonic Oscillators and Poincare-Lindstedt Perturbation Theory.

Implements Landau & Lifshitz §28: d^2 x / dt^2 + omega_0^2 x + alpha x^2 + beta x^3 = 0.
Removes secular resonances to calculate the amplitude-dependent frequency shift Delta omega(A).
"""

import numpy as np


class AnharmonicOscillator:
    """Nonlinear oscillator perturbation analysis."""

    def __init__(self, omega_0: float, alpha: float = 0.0, beta: float = 0.0, mass: float = 1.0):
        self.w0 = omega_0
        self.alpha = alpha  # Quadratic anharmonicity (cubic potential)
        self.beta = beta    # Cubic anharmonicity (quartic potential)
        self.m = mass

    def frequency_shift(self, amplitude: float) -> float:
        """Delta omega = (3 beta / (8 m omega_0) - 5 alpha^2 / (12 m^2 omega_0^3)) * A^2."""
        term_beta = (3.0 * self.beta) / (8.0 * self.m * self.w0)
        term_alpha = (5.0 * (self.alpha**2)) / (12.0 * (self.m**2) * (self.w0**3))
        return float((term_beta - term_alpha) * (amplitude**2))

    def perturbed_frequency(self, amplitude: float) -> float:
        """omega(A) = omega_0 + Delta omega(A)."""
        return self.w0 + self.frequency_shift(amplitude)
