import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kramers_kronig_dispersion import compute_real_chi_from_imag

def test_lorentz_oscillator_symmetry():
    # Lorentzian absorption peak
    omega = np.linspace(0.1, 10.0, 200)
    w0, gamma = 5.0, 0.5
    imag_chi = gamma * omega / ((w0**2 - omega**2)**2 + (gamma * omega)**2)
    real_chi = compute_real_chi_from_imag(omega, imag_chi)
    # Below resonance w < w0, real_chi > 0 (normal dispersion)
    idx_below = np.argmin(np.abs(omega - 4.0))
    assert real_chi[idx_below] > 0
