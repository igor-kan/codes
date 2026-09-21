import numpy as np
from gordon_decomposition import sigma_tensor, convective_term, spin_magnetic_operator


def test_sigma_antisymmetry():
    for mu in range(4):
        for nu in range(4):
            s1 = sigma_tensor(mu, nu)
            s2 = sigma_tensor(nu, mu)
            assert np.allclose(s1, -s2)
