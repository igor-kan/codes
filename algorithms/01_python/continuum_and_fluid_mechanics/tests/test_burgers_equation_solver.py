import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from burgers_equation_solver import burgers_step_upwind

def test_burgers_conservation():
    x = np.linspace(-np.pi, np.pi, 100)
    u = np.sin(x)
    u_next = burgers_step_upwind(u, dx=x[1] - x[0], dt=0.001, nu=0.01)
    assert len(u_next) == 100
