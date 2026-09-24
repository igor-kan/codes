import numpy as np
from arnoldi_krylov_iteration import arnoldi_iteration


def test_arnoldi():
    np.random.seed(42)
    A = np.random.randn(20, 20)
    b = np.random.randn(20)
    V, H = arnoldi_iteration(A, b, m=5)
    # Orthonormal columns
    assert np.allclose(V.T @ V, np.eye(5), atol=1e-10)
