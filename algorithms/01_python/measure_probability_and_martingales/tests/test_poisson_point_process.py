import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poisson_point_process import simulate_poisson_points_2d

def test_poisson_points_count():
    pts = simulate_poisson_points_2d(rate_lambda=100.0, seed=42)
    assert len(pts) > 50
    assert np.all((pts[:, 0] >= 0.0) & (pts[:, 0] <= 1.0))
