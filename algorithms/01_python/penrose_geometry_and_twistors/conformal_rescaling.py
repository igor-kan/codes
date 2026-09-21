"""
Conformal Transformation of metric g_{ab} -> Omega^2 g_{ab}.
Reference: Penrose, The Road to Reality, Ch. 28.
"""
import numpy as np

def conformally_rescaled_ricci_scalar(R: float, omega: float, box_omega: float, grad_omega_sq: float, dim: int = 4) -> float:
    """
    Computes transformed Ricci scalar tilde{R} under g_ab -> Omega^2 g_ab:
    tilde{R} = Omega^{-2} [ R - 2(n-1) box(Omega)/Omega - (n-1)(n-4) (grad Omega)^2 / Omega^2 ]
    For n=4, the last term vanishes identically!
    """
    n = dim
    if n == 4:
        return (R - 6.0 * (box_omega / omega)) / (omega**2)
    term2 = 2.0 * (n - 1) * (box_omega / omega)
    term3 = (n - 1) * (n - 4) * (grad_omega_sq / (omega**2))
    return (R - term2 - term3) / (omega**2)
