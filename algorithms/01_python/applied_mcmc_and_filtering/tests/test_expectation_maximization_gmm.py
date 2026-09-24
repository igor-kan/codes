import numpy as np
from expectation_maximization_gmm import em_gmm_e_step


def test_em_e_step():
    x = np.array([0.0, 10.0])
    resp = em_gmm_e_step(x, mu1=0.0, sig1=1.0, mu2=10.0, sig2=1.0, pi1=0.5)
    assert resp[0] > 0.99
    assert resp[1] < 0.01
