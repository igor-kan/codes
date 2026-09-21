import numpy as np
from bessel_beam_propagation import bessel_beam_radial_profile, axicon_nondiffracting_range


def test_bessel_profile():
    r = np.linspace(0, 1e-3, 100)
    I = bessel_beam_radial_profile(r, kr=1e4)
    assert I[0] == 1.0
    assert np.all(I >= 0.0)

    z_max = axicon_nondiffracting_range(beam_radius=5e-3, axicon_angle_rad=0.05, n_axicon=1.5)
    assert z_max > 0
