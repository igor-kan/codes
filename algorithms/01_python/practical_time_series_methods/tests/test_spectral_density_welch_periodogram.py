import numpy as np
from spectral_density_welch_periodogram import welch_psd


def test_welch():
    fs = 100.0
    t = np.arange(1000) / fs
    x = np.sin(2.0 * np.pi * 10.0 * t)
    f, psd = welch_psd(x, fs, nperseg=128)
    peak_freq = f[np.argmax(psd)]
    assert np.isclose(peak_freq, 10.0, atol=1.0)
