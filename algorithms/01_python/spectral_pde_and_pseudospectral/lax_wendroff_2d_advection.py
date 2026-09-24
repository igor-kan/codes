"""2D Lax-Wendroff Conservative Hyperbolic Advection Scheme."""
import numpy as np


def lax_wendroff_step_2d(u: np.ndarray, cx: float, cy: float) -> np.ndarray:
    """Single time step for u_t + cx * u_x + cy * u_y = 0 on periodic grid."""
    u_xp = np.roll(u, -1, axis=1)
    u_xm = np.roll(u, 1, axis=1)
    u_yp = np.roll(u, -1, axis=0)
    u_ym = np.roll(u, 1, axis=0)
    
    diff_x = -0.5 * cx * (u_xp - u_xm) + 0.5 * (cx**2) * (u_xp - 2.0 * u + u_xm)
    diff_y = -0.5 * cy * (u_yp - u_ym) + 0.5 * (cy**2) * (u_yp - 2.0 * u + u_ym)
    return u + diff_x + diff_y
