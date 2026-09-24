import numpy as np
from stationary_phase_approximation import stationary_phase_fourier


def test_stat_phase():
    z = stationary_phase_fourier(0.0, 2.0, k=100.0)
    assert np.abs(z) > 0
