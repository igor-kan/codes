import numpy as np
from biconjugate_gradient_stabilized import bicgstab


def test_bicgstab():
    A = np.array([[4.0, 1.0, -1.0],
                  [2.0, 5.0, 2.0],
                  [-1.0, 1.0, 3.0]])
    b = np.array([3.0, 9.0, 3.0])
    x = bicgstab(A, b)
    assert np.allclose(A @ x, b, atol=1e-6)
