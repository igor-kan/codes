"""
Almgren-Chriss Optimal Trade Execution Trajectory.
Reference: Almgren & Chriss (2000); Marcos Lopez de Prado.
"""
import numpy as np

def linear_liquidation_trajectory(total_shares: float, n_intervals: int) -> np.ndarray:
    """Simple constant-rate trade schedule."""
    trade_per_interval = total_shares / n_intervals
    return np.full(n_intervals, trade_per_interval)
