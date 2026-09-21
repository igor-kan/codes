import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from collision_threshold_energy import fixed_target_threshold_energy

def test_pion_production():
    # p + p -> p + p + pi0 (m_p approx 938 MeV, m_pi approx 135 MeV)
    # Threshold kinetic energy is approx 280 MeV
    m_p = 938.27
    m_pi = 134.97
    T_th = fixed_target_threshold_energy(m_p, m_p, [m_p, m_p, m_pi])
    assert 275.0 < T_th < 285.0
