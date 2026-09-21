import os, sys, numpy as np
from scipy.special import airy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from airy_function_asymptotics import airy_ai_positive_asymptotics

def test_airy_asymptotics():
    x = 5.0
    approx = airy_ai_positive_asymptotics(x)
    exact = airy(x)[0]
    assert np.isclose(approx, exact, rtol=0.02)
