import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gamow_alpha_decay import gamow_factor

def test_gamow_energy_dependence():
    # Higher energy -> smaller Gamow exponent (much faster decay)
    g_low = gamow_factor(Z_daughter=82, E_alpha_MeV=4.0)
    g_high = gamow_factor(Z_daughter=82, E_alpha_MeV=8.0)
    assert g_high < g_low
