import numpy as np
from compton_scattering_klein_nishina import compton_scattered_photon_energy, klein_nishina_diff_cross_section, M_ELECTRON, ALPHA_EM


def test_thomson_limit():
    # At very low photon energy omega << m, Klein-Nishina approaches Thomson cross section
    omega_low = 1e-7  # GeV
    theta = np.pi / 2.0
    kn = klein_nishina_diff_cross_section(omega_low, theta)
    thomson = 0.5 * (ALPHA_EM / M_ELECTRON)**2 * (1.0 + np.cos(theta)**2)
    assert np.isclose(kn, thomson, rtol=1e-3)
