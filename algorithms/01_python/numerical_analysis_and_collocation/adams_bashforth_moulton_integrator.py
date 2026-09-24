"""Adams-Bashforth-Moulton 4th-Order Predictor-Corrector ODE Integrator."""
import numpy as np
from typing import Callable


def abm4_step(f: Callable, t: np.ndarray, y: np.ndarray, h: float) -> tuple:
    """Single predictor-corrector step given previous 4 states."""
    f3, f2, f1, f0 = f(t[3], y[3]), f(t[2], y[2]), f(t[1], y[1]), f(t[0], y[0])
    # Adams-Bashforth predictor
    y_pred = y[3] + (h / 24.0) * (55.0 * f3 - 59.0 * f2 + 37.0 * f1 - 9.0 * f0)
    t_next = t[3] + h
    f_pred = f(t_next, y_pred)
    # Adams-Moulton corrector
    y_corr = y[3] + (h / 24.0) * (9.0 * f_pred + 19.0 * f3 - 5.0 * f2 + f1)
    return t_next, y_corr
