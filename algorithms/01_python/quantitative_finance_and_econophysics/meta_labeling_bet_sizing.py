"""
Bet Sizing via Probability Calibration and Sigmoid Mapping.
References: Marcos Lopez de Prado - Advances in Financial Machine Learning (Ch. 10).
"""
import numpy as np

def bet_size_sigmoid(prob: float, num_classes: int = 2) -> float:
    """Calculate signed position bet size in [-1, 1] from model probability."""
    z = (prob - 1.0 / num_classes) / np.sqrt(prob * (1.0 - prob) + 1e-8)
    return float(2.0 / (1.0 + np.exp(-z)) - 1.0)
