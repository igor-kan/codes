import numpy as np
from fresnel_equations_polarization import brewster_angle, critical_angle, fresnel_amplitudes


def test_fresnel_brewster():
    n1, n2 = 1.0, 1.5
    th_B = brewster_angle(n1, n2)
    amps = fresnel_amplitudes(th_B, n1, n2)
    # At Brewster angle, rp = 0
    assert np.isclose(abs(amps["r_p"]), 0.0, atol=1e-10)
    assert abs(amps["r_s"]) > 0


def test_total_internal_reflection():
    n1, n2 = 1.5, 1.0
    th_c = critical_angle(n1, n2)
    # Above critical angle, |rs| = |rp| = 1.0
    amps = fresnel_amplitudes(th_c + 0.1, n1, n2)
    assert np.isclose(abs(amps["r_s"]), 1.0)
    assert np.isclose(abs(amps["r_p"]), 1.0)
