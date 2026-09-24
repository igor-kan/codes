import numpy as np
from fractional_brownian_motion import generate_fractional_gaussian_noise


def test_fbm():
    fgn = generate_fractional_gaussian_noise(H=0.7, n=1024)
    assert len(fgn) == 1024
    # Check zero mean
    assert np.isclose(np.mean(fgn), 0.0, atol=0.2)
