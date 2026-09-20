"""
Conformal Mapping: Joukowsky Transform and Potential Flow.
References: Boas - Mathematical Methods in the Physical Sciences (Ch. 14).
"""
import numpy as np

def joukowsky_transform(z: np.ndarray, c: float = 1.0) -> np.ndarray:
    """Joukowsky airfoil transformation w = z + c^2 / z."""
    z = np.asarray(z, dtype=complex)
    return z + (c**2) / z

def cylinder_flow_potential(z: np.ndarray, U: float = 1.0, R: float = 1.0, circulation: float = 0.0) -> np.ndarray:
    """Complex potential F(z) for inviscid flow past a cylinder with circulation Gamma."""
    z = np.asarray(z, dtype=complex)
    # F(z) = U (z + R^2/z) + i Gamma/(2 pi) ln(z/R)
    F = U * (z + (R**2) / z)
    if circulation != 0.0:
        F += 1j * (circulation / (2 * np.pi)) * np.log(z / R)
    return F

def complex_velocity(z: np.ndarray, U: float = 1.0, R: float = 1.0, circulation: float = 0.0) -> np.ndarray:
    """Complex velocity u - i v = dF/dz."""
    z = np.asarray(z, dtype=complex)
    dF_dz = U * (1.0 - (R**2) / (z**2))
    if circulation != 0.0:
        dF_dz += 1j * (circulation / (2 * np.pi)) / z
    return dF_dz
