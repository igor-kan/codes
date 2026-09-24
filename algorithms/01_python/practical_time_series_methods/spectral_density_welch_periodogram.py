"""Welch's Averaged Modified Periodogram Spectral Density Estimation."""
import numpy as np


def welch_psd(x: np.ndarray, fs: float, nperseg: int = 128) -> tuple:
    """Estimate Power Spectral Density using Welch's Hann windowing."""
    step = nperseg // 2
    window = np.hanning(nperseg)
    scale = 1.0 / (fs * np.sum(window**2))
    
    segments = []
    for start in range(0, len(x) - nperseg + 1, step):
        seg = x[start:start + nperseg] * window
        fft_seg = np.fft.rfft(seg)
        segments.append(np.abs(fft_seg)**2 * scale)
        
    psd = np.mean(segments, axis=0)
    freqs = np.fft.rfftfreq(nperseg, d=1.0 / fs)
    return freqs, psd
