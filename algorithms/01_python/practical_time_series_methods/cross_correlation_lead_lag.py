"""Normalized Cross-Correlation and Lead-Lag Determination."""
import numpy as np


def lead_lag_correlation(x: np.ndarray, y: np.ndarray, max_lag: int) -> tuple:
    """Compute normalized cross-correlation across range [-max_lag, max_lag]."""
    x_c = x - np.mean(x)
    y_c = y - np.mean(y)
    norm = np.linalg.norm(x_c) * np.linalg.norm(y_c)
    
    lags = np.arange(-max_lag, max_lag + 1)
    corr = np.zeros(len(lags))
    for idx, lag in enumerate(lags):
        if lag > 0:
            corr[idx] = np.sum(x_c[:-lag] * y_c[lag:]) / norm
        elif lag < 0:
            corr[idx] = np.sum(x_c[-lag:] * y_c[:lag]) / norm
        else:
            corr[idx] = np.sum(x_c * y_c) / norm
    optimal_lag = lags[np.argmax(corr)]
    return lags, corr, int(optimal_lag)
