import numpy as np
from spatial_filter_pinhole import optimum_pinhole_diameter, lowpass_spatial_filter_1d


def test_spatial_filter():
    d_opt = optimum_pinhole_diameter(wavelength=632.8e-9, focal_length=0.05, beam_waist=1e-3)
    assert d_opt > 0

    # Filter out high frequency noise from DC signal
    n = 256
    dx = 1e-4
    x = np.arange(n) * dx
    clean_signal = np.ones(n)
    noisy_signal = clean_signal + 0.5 * np.cos(2.0 * np.pi * 500.0 * x)

    filtered = lowpass_spatial_filter_1d(noisy_signal, dx, cutoff_freq=100.0)
    assert np.std(filtered.real) < np.std(noisy_signal)
