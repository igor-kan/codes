import numpy as np
from kelvin_helmholtz_mhd import is_kh_stable_mhd, kh_growth_rate_unmagnetized


def test_kh_stability():
    rho1 = 1.0
    rho2 = 2.0
    delta_u = 5.0

    # Unmagnetized growth rate is positive
    growth = kh_growth_rate_unmagnetized(rho1, rho2, delta_u, k=1.0)
    assert growth > 0

    # Weak magnetic field is unstable
    assert not is_kh_stable_mhd(rho1, rho2, delta_u, B_parallel=1e-5)
    # Strong magnetic field stabilizes interface
    assert is_kh_stable_mhd(rho1, rho2, delta_u, B_parallel=1.0)
