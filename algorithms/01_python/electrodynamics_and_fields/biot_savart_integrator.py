"""
Biot-Savart Law Numerical Integrator for Arbitrary 3D Current Curves.
References: Arfken, Weber, Harris - Mathematical Methods for Physicists.
"""
import numpy as np

def biot_savart_loop(curve_points: np.ndarray, I: float, r_eval: np.ndarray, mu0: float = 1.0) -> np.ndarray:
    """
    Compute magnetic field B at r_eval produced by closed current curve:
    B = (mu0 * I / 4 pi) int (dl x R) / R^3
    """
    curve_points = np.asarray(curve_points, dtype=float)
    r_eval = np.asarray(r_eval, dtype=float)
    N = len(curve_points)

    B = np.zeros(3)
    for i in range(N):
        p1 = curve_points[i]
        p2 = curve_points[(i + 1) % N]
        dl = p2 - p1
        mid = 0.5 * (p1 + p2)
        R_vec = r_eval - mid
        R_mag = np.linalg.norm(R_vec)
        if R_mag > 1e-10:
            B += np.cross(dl, R_vec) / (R_mag**3)

    return (mu0 * I / (4.0 * np.pi)) * B
