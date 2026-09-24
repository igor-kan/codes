import numpy as np
from spherical_harmonics_transform import evaluate_spherical_harmonic


def test_sph_harm():
    Y00 = evaluate_spherical_harmonic(0, 0, np.array([0.0]), np.array([0.0]))
    # Y_0^0 = 1 / sqrt(4 * pi) approx 0.28209
    assert np.isclose(np.abs(Y00[0]), 1.0 / np.sqrt(4.0 * np.pi), atol=1e-4)
