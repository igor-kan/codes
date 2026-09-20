import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from split_operator_method import SplitOperator1D

def test_norm_preservation():
    x = np.linspace(-10, 10, 256)
    V = 0.5 * x**2  # Harmonic oscillator
    solver = SplitOperator1D(x, V)
    
    # Gaussian packet
    psi0 = (np.pi)**(-0.25) * np.exp(-0.5 * x**2).astype(complex)
    norm0 = np.trapezoid(np.abs(psi0)**2, x)
    
    psi = psi0.copy()
    for _ in range(50):
        psi = solver.step(psi, dt=0.02)
        
    norm_f = np.trapezoid(np.abs(psi)**2, x)
    assert np.isclose(norm_f, norm0, atol=1e-8)
