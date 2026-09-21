"""
Robinson-Trautman Spacetime: Twist-free, Shear-free Geodesic Null Congruences.
Reference: Penrose, The Road to Reality, Ch. 28; Stephani et al.
"""
import numpy as np

def robinson_trautman_laplacian(P: float, dP_dzeta: complex, d2P_dzeta2: complex) -> float:
    """
    Gaussian curvature K of the 2-surfaces in Robinson-Trautman geometry:
    K = 2 P^2 d^2(ln P) / (dzeta d bar{zeta}).
    """
    # K = 2 P (d^2 P / (dzeta d bar{zeta})) - 2 |dP/dzeta|^2
    term1 = 2.0 * P * (d2P_dzeta2.real)
    term2 = 2.0 * (abs(dP_dzeta)**2)
    return float(term1 - term2)
