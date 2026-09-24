import numpy as np
from empirical_mode_decomposition_emd import sifting_step


def test_sifting():
    t = np.linspace(0, 1, 100)
    sig = np.sin(2.0 * np.pi * 5.0 * t) + np.sin(2.0 * np.pi * 20.0 * t)
    imf = sifting_step(sig)
    assert len(imf) > 0
