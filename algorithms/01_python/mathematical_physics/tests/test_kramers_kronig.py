import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kramers_kronig import kramers_kronig_real_from_imag

def test_lorentzian_oscillator():
    # Lorentzian: chi(w) = 1 / (w0 - w - i*gamma) = (w0 - w) / ((w0-w)^2 + g^2) + i g / ((w0-w)^2 + g^2)
    w0 = 5.0
    gamma = 0.5
    w = np.linspace(0, 10, 1024)
    chi_exact = 1.0 / (w0 - w - 1j * gamma)
    
    chi_real_rec = kramers_kronig_real_from_imag(w, chi_exact.imag)
    # Check correlation / similarity in the peak region
    mid = slice(400, 600)
    corr = np.corrcoef(chi_real_rec[mid], chi_exact.real[mid])[0, 1]
    assert corr > 0.95
