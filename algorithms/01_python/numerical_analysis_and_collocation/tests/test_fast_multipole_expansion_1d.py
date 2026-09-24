import numpy as np
from fast_multipole_expansion_1d import multipole_moments_1d


def test_moments():
    q = np.array([1.0, -1.0])
    x = np.array([-0.5, 0.5])
    m = multipole_moments_1d(q, x, center=0.0, p_order=2)
    assert np.isclose(m[0], 0.0)  # Dipole has net zero monopole
    assert np.isclose(m[1], -1.0)
