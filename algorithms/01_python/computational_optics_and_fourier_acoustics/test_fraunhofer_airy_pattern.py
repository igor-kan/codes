import numpy as np
from fraunhofer_airy_pattern import airy_pattern_intensity, rayleigh_angular_resolution


def test_airy_disk():
    wl = 500e-9
    D = 0.05
    th_rayleigh = rayleigh_angular_resolution(wl, D)
    assert th_rayleigh > 0

    # At theta = 0, intensity is maximum I0 = 1.0
    I_center = airy_pattern_intensity(np.array([0.0]), wl, D)[0]
    assert np.isclose(I_center, 1.0)

    # At Rayleigh first zero, intensity drops close to 0
    I_zero = airy_pattern_intensity(np.array([th_rayleigh]), wl, D)[0]
    assert I_zero < 1e-4
