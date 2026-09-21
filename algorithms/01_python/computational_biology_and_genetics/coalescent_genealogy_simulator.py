"""
Kingman's Coalescent Genealogy Waiting Times Simulator.
Reference: Campbell Biology (12th Ed.), Ch. 26; Hein et al., Gene Genealogies.
"""
import numpy as np
from typing import List

def simulate_coalescent_times(sample_size: int, N_e: int, seed: int = 42) -> List[float]:
    """
    Simulates waiting times T_k while there are k lineages:
    T_k ~ Exponential(rate = k(k - 1) / (4 N_e)).
    """
    rng = np.random.default_rng(seed)
    waiting_times = []
    for k in range(sample_size, 1, -1):
        rate = (k * (k - 1)) / (4.0 * N_e)
        t_k = rng.exponential(1.0 / rate)
        waiting_times.append(float(t_k))
    return waiting_times
