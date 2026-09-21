import numpy as np
from breit_wigner_resonance import z_boson_cross_section


def test_z_peak():
    m_z = 91.1876
    sigma_peak = z_boson_cross_section(m_z)
    sigma_off_peak = z_boson_cross_section(m_z + 3.0)
    assert sigma_peak > 2.0 * sigma_off_peak
