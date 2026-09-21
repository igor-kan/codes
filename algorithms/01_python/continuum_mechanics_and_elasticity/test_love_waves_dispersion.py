import numpy as np
from love_waves_dispersion import love_wave_dispersion_relation


def test_love_bounds():
    c_T1 = 3000.0  # m/s in crust
    mu_1 = 3.0e10
    c_T2 = 4500.0  # m/s in mantle
    mu_2 = 6.0e10
    d = 10000.0    # 10 km
    omega = 0.5    # rad/s

    # Phase speed must be between c_T1 and c_T2
    c_mid = 3500.0
    res = love_wave_dispersion_relation(c_mid, omega, d, c_T1, mu_1, c_T2, mu_2)
    assert np.isfinite(res)
