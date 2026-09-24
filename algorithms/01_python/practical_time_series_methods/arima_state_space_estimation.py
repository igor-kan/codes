"""ARIMA State-Space Representation and Prediction."""
import numpy as np


def ar1_recursive_forecast(x: np.ndarray, phi: float, n_ahead: int) -> np.ndarray:
    """Generate multi-step autoregressive AR(1) forecast."""
    forecast = np.zeros(n_ahead)
    last_val = x[-1]
    for i in range(n_ahead):
        last_val = phi * last_val
        forecast[i] = last_val
    return forecast
