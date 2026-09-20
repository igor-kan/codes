import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from biot_savart_integrator import biot_savart_loop

def test_circular_loop_center():
    # Circular loop in xy-plane of radius R, field at center is mu0 I / (2 R)
    R = 1.0
    I = 1.0
    theta = np.linspace(0, 2*np.pi, 200, endpoint=False)
    circle = np.column_stack([R * np.cos(theta), R * np.sin(theta), np.zeros_like(theta)])
    
    B_center = biot_savart_loop(circle, I=I, r_eval=np.array([0.0, 0.0, 0.0]))
    expected_Bz = 1.0 / (2.0 * R)
    assert np.isclose(B_center[2], expected_Bz, rtol=1e-3)
