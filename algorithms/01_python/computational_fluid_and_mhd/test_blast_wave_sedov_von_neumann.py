import numpy as np
from blast_wave_sedov_von_neumann import sedov_shock_radius, sedov_shock_front_properties


def test_sedov_blast():
    E = 1e14  # Joules (approx 20 kilotons TNT)
    rho0 = 1.225  # kg/m^3 (sea level air)
    t = 0.01  # 10 ms

    res = sedov_shock_front_properties(E, rho0, t, gamma=1.4)
    assert res["radius"] > 0
    assert res["velocity"] > 0
    assert np.isclose(res["density"], 6.0 * rho0)  # (1.4 + 1)/(1.4 - 1) = 2.4/0.4 = 6.0
