"""Dynamic Time Warping (DTW) Sequence Alignment and Distance."""
import numpy as np


def dtw_distance(s1: np.ndarray, s2: np.ndarray) -> float:
    """Compute minimal non-linear alignment cost via dynamic programming."""
    n, m = len(s1), len(s2)
    D = np.full((n + 1, m + 1), np.inf)
    D[0, 0] = 0.0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = (s1[i - 1] - s2[j - 1])**2
            D[i, j] = cost + min(D[i - 1, j], D[i, j - 1], D[i - 1, j - 1])
            
    return float(np.sqrt(D[n, m]))
