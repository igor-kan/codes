import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fdtd_quantum_wavepacket import QuantumFDTD1D

def test_fdtd_step():
    x = np.linspace(-5, 5, 200)
    V = np.zeros_like(x)
    fdtd = QuantumFDTD1D(x, V, dt=0.001)
    pr = np.exp(-x**2)
    pi = np.zeros_like(x)
    pr_next, pi_next = fdtd.step(pr, pi)
    assert not np.allclose(pi_next, 0.0)
