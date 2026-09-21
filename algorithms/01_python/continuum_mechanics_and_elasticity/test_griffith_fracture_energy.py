import numpy as np
from griffith_fracture_energy import critical_fracture_stress, stress_intensity_factor_mode1


def test_fracture():
    E = 70.0e9  # Glass 70 GPa
    nu = 0.22
    gamma_s = 1.0  # J/m^2
    a = 1e-3  # 1 mm half-crack

    sig_c = critical_fracture_stress(a, gamma_s, E, nu, plane_strain=True)
    K_Ic = stress_intensity_factor_mode1(sig_c, a)
    assert sig_c > 0
    assert K_Ic > 0
