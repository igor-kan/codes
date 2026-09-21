import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nuclear_q_value import reaction_q_value

def test_deuteron_fusion():
    # d + d -> He-3 + n (Q approx +3.27 MeV)
    m_d = 2.014102
    m_he3 = 3.016029
    m_n = 1.008665
    Q = reaction_q_value([m_d, m_d], [m_he3, m_n])
    assert np.isclose(Q, 3.27, atol=0.05)
