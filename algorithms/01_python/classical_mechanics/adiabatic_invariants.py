"""Adiabatic Invariants in Classical Mechanics: J = oint p dq approx const.

Implements Landau & Lifshitz §49 and Arnold §48:
For slowly varying system parameters (dot{lambda} / lambda << omega), action integral J remains invariant to first order.
"""

from typing import Sequence, Tuple
import numpy as np


class AdiabaticInvariantOscillator:
    """Harmonic oscillator with slowly time-dependent frequency omega(t)."""

    def __init__(self, omega_func):
        self.w_func = omega_func

    def evaluate_energy(self, q: float, p: float, mass: float, t: float) -> float:
        """E(t) = 1/2 p^2 / m + 1/2 m omega(t)^2 q^2."""
        w = self.w_func(t)
        return 0.5 * (p**2) / mass + 0.5 * mass * (w**2) * (q**2)

    def action_variable(self, q: float, p: float, mass: float, t: float) -> float:
        """J = E(t) / omega(t) is the adiabatic invariant."""
        e = self.evaluate_energy(q, p, mass, t)
        w = self.w_func(t)
        return e / w
