"""
Zero-order Hankel Transform (Fourier-Bessel Transform): H_0[f](k) = int_0^infty r f(r) J_0(k r) dr.
Reference: Blennow, Ch. 6.
"""
import numpy as np
from scipy.special import j0

def hankel_transform_order0(f_func, k_vals: np.ndarray, r_max: float = 20.0, n_pts: int = 1000) -> np.ndarray:
    r = np.linspace(1e-4, r_max, n_pts)
    dr = r[1] - r[0]
    f_r = np.array([f_func(ri) for ri in r])
    out = np.zeros_like(k_vals, dtype=float)
    
    for i, k in enumerate(k_vals):
        kernel = r * f_r * j0(k * r)
        out[i] = np.trapz(kernel, dx=dr)
    return out
