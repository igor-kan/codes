import numpy as np
from zernike_polynomials import zernike_polynomial, zernike_radial


def test_zernike_defocus():
    rho = np.array([0.0, 0.5, 1.0])
    # Defocus R_2^0(rho) = 2*rho^2 - 1
    R20 = zernike_radial(2, 0, rho)
    expected = 2.0 * (rho**2) - 1.0
    assert np.allclose(R20, expected)


def test_zernike_spherical():
    rho = np.array([0.0, 0.5, 1.0])
    # Spherical R_4^0(rho) = 6*rho^4 - 6*rho^2 + 1
    R40 = zernike_radial(4, 0, rho)
    expected = 6.0 * (rho**4) - 6.0 * (rho**2) + 1.0
    assert np.allclose(R40, expected)
