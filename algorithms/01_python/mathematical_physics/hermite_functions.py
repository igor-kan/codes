"""
Hermite Polynomials & Quantum Harmonic Oscillator Wavefunctions.
References: Boas - Mathematical Methods in the Physical Sciences.
"""
import numpy as np
import math

def hermite_polynomial(n: int, x: np.ndarray) -> np.ndarray:
    """Evaluate physicist's Hermite polynomial H_n(x)."""
    x = np.asarray(x, dtype=float)
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return 2.0 * x
    
    h0 = np.ones_like(x)
    h1 = 2.0 * x
    for k in range(1, n):
        h2 = 2.0 * x * h1 - 2.0 * k * h0
        h0, h1 = h1, h2
    return h1

def harmonic_oscillator_psi(n: int, x: np.ndarray) -> np.ndarray:
    """Normalized 1D quantum harmonic oscillator wavefunction psi_n(x)."""
    norm = 1.0 / np.sqrt(2**n * math.factorial(n) * np.sqrt(np.pi))
    return norm * hermite_polynomial(n, x) * np.exp(-0.5 * x**2)
