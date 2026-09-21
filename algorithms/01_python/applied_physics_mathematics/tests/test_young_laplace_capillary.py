import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from young_laplace_capillary import jurin_capillary_height

def test_water_in_glass_capillary():
    # Water at 20 C: gamma = 0.0728 N/m, rho = 1000 kg/m^3, theta = 0, r = 0.5 mm
    h = jurin_capillary_height(0.0728, 0.0, 0.0005, 1000.0)
    # Approx 2.97 cm
    assert 0.025 < h < 0.035
