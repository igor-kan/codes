import numpy as np
from von_mises_yield import von_mises_stress, check_yield


def test_uniaxial_tension():
    # In uniaxial tension sigma_xx = sigma_0, von Mises and Tresca stress both equal sigma_0
    sig0 = 250.0e6  # 250 MPa
    sigma = np.zeros((3, 3))
    sigma[0, 0] = sig0

    res = check_yield(sigma, 250.0e6)
    assert np.isclose(res["von_mises_stress"], sig0)
    assert np.isclose(res["tresca_stress"], sig0)
    assert res["von_mises_yielded"] is True
