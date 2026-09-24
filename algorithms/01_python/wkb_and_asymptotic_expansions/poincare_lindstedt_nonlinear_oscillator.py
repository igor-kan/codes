"""Poincare-Lindstedt Perturbation Method for Duffing Oscillator Frequency Shift.

x'' + x + eps * x^3 = 0.
Corrected natural frequency: omega(eps) = 1 + (3/8) * eps * A^2.
"""
def poincare_lindstedt_duffing_freq(A: float, eps: float) -> float:
    """Shifted frequency omega to eliminate secular resonances."""
    return float(1.0 + (3.0 / 8.0) * eps * (A**2))
