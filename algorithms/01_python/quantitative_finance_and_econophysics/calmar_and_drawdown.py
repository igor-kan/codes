"""
Maximum Drawdown (MDD) and Calmar Ratio.
References: Marcos Lopez de Prado - Advances in Financial Machine Learning.
"""
import numpy as np

def max_drawdown(equity_curve: np.ndarray) -> float:
    """Calculate Maximum Drawdown as maximum peak-to-trough decline."""
    peaks = np.maximum.accumulate(equity_curve)
    drawdowns = (peaks - equity_curve) / peaks
    return float(np.max(drawdowns))

def calmar_ratio(returns: np.ndarray, equity_curve: np.ndarray, periods_per_year: int = 252) -> float:
    """Calmar ratio = Annualized Return / Maximum Drawdown."""
    mdd = max_drawdown(equity_curve)
    if mdd == 0:
        return float('inf')
    ann_return = np.mean(returns) * periods_per_year
    return float(ann_return / mdd)
