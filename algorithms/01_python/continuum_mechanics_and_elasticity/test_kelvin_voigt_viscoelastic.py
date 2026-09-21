import numpy as np
from kelvin_voigt_viscoelastic import kelvin_voigt_creep, kelvin_voigt_dynamic_modulus


def test_kelvin_voigt():
    E = 1.0e6
    eta = 1.0e7
    sigma_0 = 1.0e5

    # At t=0, strain is 0 (dashpot resists instantaneous jump)
    eps_0 = kelvin_voigt_creep(0.0, sigma_0, E, eta)
    assert np.isclose(eps_0, 0.0)

    # At large t, strain reaches asymptotic elastic limit sigma_0 / E
    eps_inf = kelvin_voigt_creep(1e4, sigma_0, E, eta)
    assert np.isclose(eps_inf, sigma_0 / E, rtol=1e-5)
