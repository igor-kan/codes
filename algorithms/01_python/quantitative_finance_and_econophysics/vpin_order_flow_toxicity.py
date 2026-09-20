"""
Volume-Synchronized Probability of Toxicity (VPIN).
References: Marcos Lopez de Prado - Advances in Financial Machine Learning.
"""
import numpy as np

def compute_vpin(buy_volumes: np.ndarray, sell_volumes: np.ndarray, bucket_volume: float) -> float:
    """Calculate VPIN = sum |V_B - V_S| / (N * V)."""
    imbalance = np.abs(buy_volumes - sell_volumes)
    total_volume = len(buy_volumes) * bucket_volume
    return float(np.sum(imbalance) / total_volume)
