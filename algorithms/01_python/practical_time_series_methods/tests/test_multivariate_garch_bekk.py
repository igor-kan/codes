import numpy as np
from multivariate_garch_bekk import bekk_covariance_step


def test_bekk():
    C = np.array([[0.1, 0.0], [0.05, 0.1]])
    A = 0.2 * np.eye(2)
    B = 0.8 * np.eye(2)
    eps = np.array([0.5, -0.5])
    H_prev = 0.04 * np.eye(2)
    H_next = bekk_covariance_step(C, A, B, eps, H_prev)
    # Positive definite
    eigvals = np.linalg.eigvalsh(H_next)
    assert np.all(eigvals > 0.0)
