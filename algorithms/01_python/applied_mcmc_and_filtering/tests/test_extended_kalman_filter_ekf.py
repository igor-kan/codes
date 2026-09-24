import numpy as np
from extended_kalman_filter_ekf import ekf_update


def test_ekf():
    x0 = np.array([1.0])
    P0 = np.array([[1.0]])
    z = np.array([1.2])
    h = lambda x: x
    H = np.array([[1.0]])
    R = np.array([[0.1]])
    x1, P1 = ekf_update(x0, P0, z, h, H, R)
    assert P1[0, 0] < P0[0, 0]
