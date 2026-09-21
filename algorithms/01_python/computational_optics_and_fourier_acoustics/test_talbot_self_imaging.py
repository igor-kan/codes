import numpy as np
from talbot_self_imaging import talbot_distance, fractional_talbot_distance


def test_talbot():
    a = 10e-6  # 10 um pitch grating
    wl = 500e-9  # 500 nm green
    z_t = talbot_distance(a, wl)
    assert np.isclose(z_t, 4e-4)  # 0.4 mm

    z_half = fractional_talbot_distance(a, wl, 1, 2)
    assert np.isclose(z_half, 0.5 * z_t)
