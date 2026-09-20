import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from svd_decomposition import svd_pseudoinverse, low_rank_svd_approx

def test_pinv_least_squares():
    A = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    b = np.array([1.0, 2.0, 3.0])
    A_pinv = svd_pseudoinverse(A)
    x = A_pinv @ b
    # Check Moore-Penrose condition A A^+ A = A
    assert np.allclose(A @ A_pinv @ A, A)

def test_low_rank_approx():
    A = np.outer([1, 2, 3], [4, 5, 6])  # Rank 1 matrix
    approx = low_rank_svd_approx(A, 1)
    assert np.allclose(approx, A)
