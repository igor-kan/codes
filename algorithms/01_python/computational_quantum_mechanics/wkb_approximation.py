"""
WKB Semiclassical Quantization and Barrier Tunneling.
References: Landau & Lifshitz - Quantum Mechanics (Vol. 3, Ch. 7).
"""
import numpy as np

def wkb_bohr_sommerfeld_action(v_func, E: float, x_min: float, x_max: float, m: float = 1.0, n_points: int = 500) -> float:
    """Compute action integral int_{x1}^{x2} sqrt(2m(E - V(x))) dx."""
    x = np.linspace(x_min, x_max, n_points)
    v_vals = v_func(x)
    p_sq = np.maximum(0.0, 2.0 * m * (E - v_vals))
    p = np.sqrt(p_sq)
    return float(np.trapezoid(p, x))

def wkb_gamow_factor(v_func, E: float, x1: float, x2: float, m: float = 1.0, hbar: float = 1.0) -> float:
    """Gamow tunneling transmission factor T = exp(-2/hbar int_{x1}^{x2} sqrt(2m(V(x) - E)) dx)."""
    x = np.linspace(x1, x2, 500)
    v_vals = v_func(x)
    kappa = np.sqrt(np.maximum(0.0, 2.0 * m * (v_vals - E)))
    integral = np.trapezoid(kappa, x)
    return float(np.exp(-2.0 * integral / hbar))
