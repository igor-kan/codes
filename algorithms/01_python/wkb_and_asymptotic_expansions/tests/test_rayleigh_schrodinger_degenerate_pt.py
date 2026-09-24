import numpy as np
from rayleigh_schrodinger_degenerate_pt import degenerate_subspace_split


def test_degenerate():
    V = np.array([[0.0, 0.2], [0.2, 0.0]])
    energies = degenerate_subspace_split(5.0, V)
    assert np.allclose(energies, [4.8, 5.2])
