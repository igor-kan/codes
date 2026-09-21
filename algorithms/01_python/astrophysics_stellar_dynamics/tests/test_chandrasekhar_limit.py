import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from chandrasekhar_limit import chandrasekhar_mass

def test_chandra_mass_order():
    m_ch = chandrasekhar_mass(mu_e=2.0)
    m_sun = 1.98847e30
    m_ch_solar = m_ch / m_sun
    # Order of magnitude check (approx 1.17 to 1.46 solar masses depending on exact mu_e and relativistic corrections)
    assert 1.10 < m_ch_solar < 1.50
