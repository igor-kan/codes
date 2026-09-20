"""
Symmetric CUSUM Filter for Event-Driven Sampling.
References: Marcos Lopez de Prado - Advances in Financial Machine Learning (Ch. 2).
"""
import numpy as np

def cusum_filter_events(returns: np.ndarray, threshold: float) -> list:
    """Identify change-point event timestamps using symmetric CUSUM filter."""
    events = []
    s_pos = 0.0
    s_neg = 0.0
    for idx, r in enumerate(returns):
        s_pos = max(0.0, s_pos + r)
        s_neg = min(0.0, s_neg + r)
        if s_pos > threshold:
            events.append(idx)
            s_pos = 0.0
        elif s_neg < -threshold:
            events.append(idx)
            s_neg = 0.0
    return events
