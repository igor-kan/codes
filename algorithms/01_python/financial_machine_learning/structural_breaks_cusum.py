"""
Symmetric CUSUM Filter for Structural Break and Regime Sampling.
Reference: Marcos Lopez de Prado, Advances in Financial Machine Learning, Ch. 2.
"""
import numpy as np
from typing import List

def cusum_filter(returns: np.ndarray, threshold: float) -> List[int]:
    """Detects events when cumulative return exceeds threshold h."""
    events = []
    s_pos = 0.0
    s_neg = 0.0
    
    for i, r in enumerate(returns):
        s_pos = max(0.0, s_pos + r)
        s_neg = min(0.0, s_neg + r)
        
        if s_pos > threshold:
            events.append(i)
            s_pos = 0.0
        elif s_neg < -threshold:
            events.append(i)
            s_neg = 0.0
            
    return events
