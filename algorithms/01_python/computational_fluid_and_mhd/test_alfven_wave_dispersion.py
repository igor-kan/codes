import numpy as np
from alfven_wave_dispersion import alfven_speed, sound_speed, magnetosonic_speeds


def test_parallel_propagation():
    # When theta = 0 (parallel to B), fast speed is max(c_s, v_A) and slow is min(c_s, v_A)
    B0 = 1e-4   # Tesla
    rho0 = 1e-12  # kg/m^3
    P0 = 1e-2   # Pa
    gamma = 5.0 / 3.0
    v_fast, v_med, v_slow = magnetosonic_speeds(B0, rho0, P0, gamma, 0.0)
    v_a = alfven_speed(B0, rho0)
    c_s = sound_speed(gamma, P0, rho0)

    assert np.isclose(v_fast, max(v_a, c_s))
    assert np.isclose(v_slow, min(v_a, c_s))
    assert np.isclose(v_med, v_a)
