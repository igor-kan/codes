"""
Colored 1/f^alpha Noise Generator via Spectral Synthesis.
References: Gershenfeld - The Nature of Mathematical Modeling.
"""
import numpy as np

def generate_colored_noise(n_samples: int, alpha: float) -> np.ndarray:
    """Generate 1/f^alpha colored noise (alpha=0: white, alpha=1: pink, alpha=2: Brownian)."""
    white = np.random.normal(size=n_samples)
    fft_white = np.fft.rfft(white)
    freqs = np.fft.rfftfreq(n_samples)
    freqs[0] = 1.0  # avoid division by zero
    
    # Filter amplitude by 1 / f^(alpha / 2)
    filter_amp = 1.0 / (freqs**(0.5 * alpha))
    filter_amp[0] = 0.0  # zero mean
    
    filtered_fft = fft_white * filter_amp
    colored = np.fft.irfft(filtered_fft, n=n_samples)
    return colored / np.std(colored)
