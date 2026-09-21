import numpy as np
from debye_shielding_sheath import debye_length, electron_plasma_frequency, bohm_sound_speed


def test_plasma_parameters():
    ne = 1e19  # m^-3
    Te = 10.0  # 10 eV
    m_p = 1.67e-27  # proton mass

    ld = debye_length(ne, Te)
    omega_pe = electron_plasma_frequency(ne)
    cs = bohm_sound_speed(Te, m_p)

    assert ld > 0
    assert omega_pe > 0
    assert cs > 0
