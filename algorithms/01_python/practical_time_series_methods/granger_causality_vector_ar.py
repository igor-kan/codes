"""Bivariate Granger Causality F-Test."""
import numpy as np
from scipy.stats import f


def granger_f_stat(y: np.ndarray, x: np.ndarray, p_lags: int = 2) -> float:
    """Compute F-statistic testing whether x Granger-causes y."""
    n = len(y) - p_lags
    Y = y[p_lags:]
    
    # Restricted model: y on lagged y
    X_restr = np.column_stack([y[p_lags - i - 1:-i - 1] for i in range(p_lags)])
    beta_r = np.linalg.lstsq(X_restr, Y, rcond=None)[0]
    rss_r = np.sum((Y - X_restr @ beta_r)**2)
    
    # Unrestricted model: y on lagged y and lagged x
    X_x = np.column_stack([x[p_lags - i - 1:-i - 1] for i in range(p_lags)])
    X_unr = np.column_stack([X_restr, X_x])
    beta_u = np.linalg.lstsq(X_unr, Y, rcond=None)[0]
    rss_u = np.sum((Y - X_unr @ beta_u)**2)
    
    f_stat = ((rss_r - rss_u) / p_lags) / (rss_u / (n - 2 * p_lags))
    return float(f_stat)
