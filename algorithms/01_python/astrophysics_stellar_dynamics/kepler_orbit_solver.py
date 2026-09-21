"""
Kepler's Equation Solver for Elliptic and Hyperbolic Orbits.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 2).
"""
import numpy as np

def solve_kepler_elliptic(M: float, e: float, tol: float = 1e-10, max_iter: int = 100) -> float:
    """Solve Kepler's equation M = E - e sin(E) using Newton-Raphson."""
    M = M % (2.0 * np.pi)
    E = M if e < 0.8 else np.pi
    for _ in range(max_iter):
        f = E - e * np.sin(E) - M
        f_prime = 1.0 - e * np.cos(E)
        dE = f / f_prime
        E -= dE
        if abs(dE) < tol:
            break
    return float(E)

def true_anomaly_from_eccentric(E: float, e: float) -> float:
    """Compute true anomaly nu: tan(nu/2) = sqrt((1+e)/(1-e)) tan(E/2)."""
    return float(2.0 * np.arctan2(np.sqrt(1.0 + e) * np.sin(0.5 * E),
                                  np.sqrt(1.0 - e) * np.cos(0.5 * E)))

def orbital_radius(a: float, e: float, nu: float) -> float:
    """Distance r = a(1 - e^2) / (1 + e cos(nu))."""
    return float(a * (1.0 - e**2) / (1.0 + e * np.cos(nu)))
