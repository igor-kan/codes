import numpy as np
from mueller_stokes_formalism import degree_of_polarization, ideal_depolarizer


def test_stokes():
    # Completely unpolarized light
    s_unpol = np.array([1.0, 0.0, 0.0, 0.0])
    dop, dolp, docp = degree_of_polarization(s_unpol)
    assert dop == 0.0

    # Linearly polarized
    s_lin = np.array([1.0, 1.0, 0.0, 0.0])
    dop_l, dolp_l, _ = degree_of_polarization(s_lin)
    assert dop_l == 1.0
    assert dolp_l == 1.0
