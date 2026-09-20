import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from qr_decomposition import householder_qr

def test_qr_orthogonality():
    A = np.array([[12.0, -51.0, 4.0], [6.0, 167.0, -68.0], [-4.0, 24.0, -41.0]])
    Q, R = householder_qr(A)
    # Check Q^T Q = I
    assert np.allclose(Q.T @ Q, np.eye(3), atol=1e-10)
    # Check QR = A
    assert np.allclose(Q @ R, A, atol=1e-10)
    # Check R is upper triangular
    assert np.allclose(np.tril(R, -1), 0.0, atol=1e-10)
