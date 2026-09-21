"""
Ornstein-Uhlenbeck Continuous Mean-Reversion Calibration and Half-Life.
Reference: Pal, Practical Time Series Analysis; Prado.
"""
import numpy as np
from typing import Tuple

def fit_ou_process(prices: np.ndarray, dt: float = 1.0) -> Tuple[float, float, float]:
    """
    Fits dx_t = theta (mu - x_t) dt + sigma dW_t via OLS on x_{t+1} - x_t = a + b x_t.
    theta = -b / dt, mu = -a / b, half_life = ln(2) / theta.
    """
    x = prices[:-1]
    dx = np.diff(prices)
    b, a = np.polyfit(x, dx, 1)
    theta = -b / dt
    mu = -a / b if b != 0 else np.mean(prices)
    half_life = np.log(2.0) / theta if theta > 0 else np.inf
    return float(theta), float(mu), float(half_life)
