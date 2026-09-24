import numpy as np
from particle_filter_sir_resampling import systematic_resample


def test_resample():
    w = np.array([0.1, 0.7, 0.2])
    idx = systematic_resample(w)
    assert len(idx) == 3
