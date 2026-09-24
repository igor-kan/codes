import numpy as np
from matched_asymptotic_boundary_layer import matched_composite_solution


def test_matched():
    x = np.array([0.0, 1.0])
    y = matched_composite_solution(x, eps=0.01)
    assert np.isclose(y[0], -1.0)
