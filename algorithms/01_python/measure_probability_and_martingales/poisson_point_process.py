"""
Simulation of 2D Spatial Poisson Point Process with Intensity Lambda.
Reference: Evans & Rosenthal, Probability and Statistics.
"""
import numpy as np

def simulate_poisson_points_2d(rate_lambda: float, x_bounds=(0.0, 1.0), y_bounds=(0.0, 1.0), seed: int = 42) -> np.ndarray:
    """
    Generates Poisson point process in [x_min, x_max] x [y_min, y_max].
    N ~ Poisson(lambda * Area).
    """
    rng = np.random.default_rng(seed)
    area = (x_bounds[1] - x_bounds[0]) * (y_bounds[1] - y_bounds[0])
    n_points = rng.poisson(rate_lambda * area)
    
    xs = rng.uniform(x_bounds[0], x_bounds[1], size=n_points)
    ys = rng.uniform(y_bounds[0], y_bounds[1], size=n_points)
    return np.column_stack([xs, ys])
