import numpy as np
from dirac_propagator import dirac_propagator_momentum, energy_projection_operators
from feynman_slash import minkowski_dot


def test_dirac_projection():
    m = 2.0
    p = np.array([np.sqrt(m**2 + 3.0), 1.0, 1.0, 1.0])
    lp, lm = energy_projection_operators(p, m)

    # Completeness: Lambda_+ + Lambda_- = I
    assert np.allclose(lp + lm, np.eye(4, dtype=complex), atol=1e-10)
    # Orthogonality: Lambda_+ * Lambda_- = 0
    assert np.allclose(lp @ lm, np.zeros((4, 4), dtype=complex), atol=1e-10)
