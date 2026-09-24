import numpy as np
from householder_qr_decomposition import qr_householder


def test_householder_qr():
    A = np.array([[12.0, -51.0, 4.0],
                  [6.0, 167.0, -68.0],
                  [-4.0, 24.0, -41.0]])
    Q, R = qr_householder(A)
    # Orthogonality
    assert np.allclose(Q.T @ Q, np.eye(3), atol=1e-10)
    # Reconstruction
    assert np.allclose(Q @ R, A, atol=1e-10)
    # Upper triangular
    assert np.allclose(np.tril(R, -1), 0.0, atol=1e-10)
