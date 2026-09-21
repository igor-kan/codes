import numpy as np
from isotropic_hooke_law import lame_from_young_poisson, stress_from_strain, strain_from_stress, bulk_modulus


def test_hooke_inversion():
    E = 210.0e9  # Steel 210 GPa
    nu = 0.30
    eps = np.array([[1e-3, 2e-4, 0], [2e-4, -3e-4, 0], [0, 0, 1e-4]])

    sigma = stress_from_strain(eps, E, nu)
    eps_recovered = strain_from_stress(sigma, E, nu)
    assert np.allclose(eps, eps_recovered, atol=1e-10)

    K = bulk_modulus(E, nu)
    lam, mu = lame_from_young_poisson(E, nu)
    assert np.isclose(K, lam + 2.0 * mu / 3.0)
