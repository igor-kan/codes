import numpy as np
from rayleigh_surface_waves import wave_speeds, rayleigh_wave_speed


def test_rayleigh_speed():
    E = 200.0e9
    nu = 0.25
    rho = 7800.0

    c_L, c_T = wave_speeds(E, nu, rho)
    c_R = rayleigh_wave_speed(E, nu, rho)

    # c_R < c_T < c_L always
    assert c_R < c_T < c_L
    # For nu = 0.25 (Poisson solid), c_R / c_T approx 0.9194
    assert np.isclose(c_R / c_T, 0.9194, atol=1e-3)
