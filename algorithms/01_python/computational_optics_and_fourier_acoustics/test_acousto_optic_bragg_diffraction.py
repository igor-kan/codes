import numpy as np
from acousto_optic_bragg_diffraction import aom_bragg_angle, aom_diffraction_efficiency


def test_aom_bragg():
    wl = 1064e-9
    fa = 80e6  # 80 MHz acoustic wave
    v_s = 4000.0  # m/s in crystal (TeO2 / quartz)
    th_B = aom_bragg_angle(wl, fa, v_s)
    assert th_B > 0

    eff = aom_diffraction_efficiency(L_interaction=0.01, optical_wavelength=wl, acoustic_power_density=1e4)
    assert 0.0 <= eff <= 1.0
