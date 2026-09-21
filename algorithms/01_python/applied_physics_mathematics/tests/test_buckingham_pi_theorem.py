import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from buckingham_pi_theorem import compute_dimensionless_groups

def test_simple_pendulum_pi():
    # Variables: Period T [T], Length L [L], Mass m [M], Gravity g [L T^-2]
    # Rows: [M, L, T]
    # Cols: [T, L, m, g]
    M = np.array([
        [0.0, 0.0, 1.0, 0.0],  # Mass M
        [0.0, 1.0, 0.0, 1.0],  # Length L
        [1.0, 0.0, 0.0, -2.0]  # Time T
    ])
    pi_basis = compute_dimensionless_groups(M)
    # 4 variables - 3 dimensions = 1 dimensionless group
    assert pi_basis.shape[1] == 1
    # Check that M @ pi == 0
    assert np.allclose(M @ pi_basis, 0.0)
