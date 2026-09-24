"""Tempered Transitions for Navigating High Energy Barriers in Multimodal Landscapes."""
import numpy as np


def geometric_temperature_ladder(n_levels: int, beta_min: float = 0.01, beta_max: float = 1.0) -> np.ndarray:
    """Construct geometric inverse-temperature ladder beta_0 < beta_1 < ... < beta_N."""
    return np.geomspace(beta_min, beta_max, n_levels)
