import numpy as np
from unscented_kalman_filter_ukf import generate_sigma_points


def test_sigma_points():
    x = np.array([0.0, 0.0])
    P = np.eye(2)
    pts, Wm, Wc = generate_sigma_points(x, P)
    assert pts.shape == (5, 2)
    assert np.isclose(np.sum(Wm), 1.0)
