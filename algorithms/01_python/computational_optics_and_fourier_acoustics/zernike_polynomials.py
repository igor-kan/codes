"""Zernike Circular Wavefront Aberration Polynomials.

Z_n^m(rho, phi) = R_n^|m|(rho) * cos(m * phi) (m >= 0) or sin(|m| * phi) (m < 0).
Radial polynomial: R_n^m(rho) = sum_k (-1)^k (n - k)! / [k! ((n+m)/2 - k)! ((n-m)/2 - k)!] * rho^(n - 2k).
Includes:
Z_0^0: Piston (1)
Z_1^-1: Tilt Y (2 rho sin phi)
Z_1^1: Tilt X (2 rho cos phi)
Z_2^0: Defocus (sqrt(3) * (2 rho^2 - 1))
Z_2^-2, Z_2^2: Astigmatism
Z_3^-1, Z_3^1: Coma
Z_4^0: Spherical aberration (sqrt(5) * (6 rho^4 - 6 rho^2 + 1))
"""
import numpy as np
import math


def zernike_radial(n: int, m: int, rho: np.ndarray) -> np.ndarray:
    """Compute radial Zernike polynomial R_n^m(rho) for 0 <= rho <= 1."""
    m_abs = abs(m)
    if (n - m_abs) % 2 != 0:
        return np.zeros_like(rho)
    
    R = np.zeros_like(rho, dtype=float)
    max_k = (n - m_abs) // 2
    for k in range(max_k + 1):
        num = (-1)**k * math.factorial(n - k)
        den = (math.factorial(k) *
               math.factorial((n + m_abs) // 2 - k) *
               math.factorial((n - m_abs) // 2 - k))
        R += (num / den) * (rho**(n - 2 * k))
    return R


def zernike_polynomial(n: int, m: int, rho: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """Compute 2D Zernike function Z_n^m(rho, phi)."""
    R = zernike_radial(n, m, rho)
    if m >= 0:
        return R * np.cos(m * phi)
    else:
        return R * np.sin(abs(m) * phi)
