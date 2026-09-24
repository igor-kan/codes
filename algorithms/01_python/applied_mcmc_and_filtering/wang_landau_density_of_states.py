"""Wang-Landau Flat-Histogram Sampling for Density of States g(E)."""
import numpy as np


def wang_landau_update(log_dos: np.ndarray, hist: np.ndarray, bin_idx: int, log_f: float) -> tuple:
    """Update log density of states and visitation histogram."""
    log_dos[bin_idx] += log_f
    hist[bin_idx] += 1
    return log_dos, hist
