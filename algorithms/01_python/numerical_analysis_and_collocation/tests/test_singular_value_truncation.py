import numpy as np
from singular_value_truncation import truncated_svd_approximation


def test_tsvd():
    A = np.outer(np.array([1, 2, 3]), np.array([4, 5, 6]))
    A_approx, energy = truncated_svd_approximation(A, rank=1)
    assert np.isclose(energy, 1.0)
    assert np.allclose(A, A_approx)
