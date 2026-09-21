"""
Wiener-Hopf Plus/Minus Function Decomposition on the Real Axis.
Reference: Hassani; Noble, Methods Based on the Wiener-Hopf Technique.
"""
import numpy as np
from typing import Tuple

def decompose_analytic_halfplanes(f_vals: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Decomposes function F(x) = F_+(x) + F_-(x) where F_+ is analytic in upper half-plane
    and F_- is analytic in lower half-plane using Fourier projection (Plemelj-Sokhotski).
    """
    F_fourier = np.fft.fft(f_vals)
    n = len(f_vals)
    mask_plus = np.zeros(n)
    mask_minus = np.zeros(n)
    
    mask_plus[:n//2] = 1.0
    mask_minus[n//2:] = 1.0
    
    f_plus = np.fft.ifft(F_fourier * mask_plus)
    f_minus = np.fft.ifft(F_fourier * mask_minus)
    return f_plus, f_minus
