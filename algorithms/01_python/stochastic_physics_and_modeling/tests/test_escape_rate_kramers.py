import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from escape_rate_kramers import kramers_escape_rate

def test_kramers_arrhenius():
    # As T increases, rate increases exponentially
    r_low = kramers_escape_rate(1.0, 1.0, 1.0, 1.0, kBT=0.5)
    r_high = kramers_escape_rate(1.0, 1.0, 1.0, 1.0, kBT=1.0)
    assert r_high > r_low
