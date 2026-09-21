"""
High-Low Parkinson and OHLC Garman-Klass Volatility Estimators.
Reference: Marcos Lopez de Prado; Parkinson (1980).
"""
import numpy as np

def parkinson_volatility(highs: np.ndarray, lows: np.ndarray) -> float:
    """sigma = sqrt( (1 / (4 ln 2 N)) sum ln(H_i / L_i)^2 )."""
    n = len(highs)
    term = np.log(highs / lows)**2
    return float(np.sqrt(np.sum(term) / (4.0 * np.log(2.0) * n)))
