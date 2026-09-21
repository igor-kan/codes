import numpy as np
from tearing_mode_reconnection import lundquist_number, sweet_parker_reconnection_rate, fkr_tearing_growth_rate


def test_reconnection_scaling():
    S = 1e8  # Typical solar coronal Lundquist number
    sp_rate = sweet_parker_reconnection_rate(S)
    assert np.isclose(sp_rate, 1e-4)

    tearing_rate = fkr_tearing_growth_rate(S)
    assert tearing_rate > 0.0  # Tearing instability is much faster than steady Sweet-Parker
