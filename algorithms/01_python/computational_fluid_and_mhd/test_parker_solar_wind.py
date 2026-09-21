import numpy as np
from parker_solar_wind import parker_critical_radius, parker_mach_number


def test_parker_sonic_point():
    T = 1.5e6  # 1.5 million Kelvin solar corona
    a, r_c = parker_critical_radius(T)
    assert r_c > 0

    # At critical radius r = r_c, Mach number is exactly 1.0
    M_crit = parker_mach_number(r_c, r_c)
    assert np.isclose(M_crit, 1.0)

    # Subsonic below r_c, supersonic above r_c
    M_sub = parker_mach_number(0.5 * r_c, r_c)
    M_super = parker_mach_number(2.0 * r_c, r_c)
    assert M_sub < 1.0
    assert M_super > 1.0
