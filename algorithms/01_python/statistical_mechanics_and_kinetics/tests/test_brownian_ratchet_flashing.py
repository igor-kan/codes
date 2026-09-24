import numpy as np
from brownian_ratchet_flashing import simulate_flashing_ratchet


def test_ratchet():
    x_final = simulate_flashing_ratchet(500, period=25)
    assert not np.isnan(x_final)
