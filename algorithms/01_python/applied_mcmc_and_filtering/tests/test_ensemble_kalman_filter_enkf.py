import numpy as np
from ensemble_kalman_filter_enkf import enkf_analysis_step


def test_enkf():
    ens = np.random.randn(2, 50)
    z = np.array([1.0, 1.0])
    H = np.eye(2)
    R = 0.1 * np.eye(2)
    ens_updated = enkf_analysis_step(ens, z, H, R)
    assert ens_updated.shape == (2, 50)
