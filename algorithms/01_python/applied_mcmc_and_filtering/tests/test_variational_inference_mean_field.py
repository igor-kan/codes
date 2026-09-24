import numpy as np
from variational_inference_mean_field import cavi_gaussian_update


def test_cavi():
    data = np.array([2.0, 2.2, 1.8])
    m, s2 = cavi_gaussian_update(data, mu0=0.0, sigma0_sq=10.0, sigma_sq=1.0)
    assert np.isclose(m, 2.0, atol=0.2)
