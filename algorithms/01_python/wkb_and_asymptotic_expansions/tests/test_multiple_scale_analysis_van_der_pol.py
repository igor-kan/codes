import numpy as np
from multiple_scale_analysis_van_der_pol import van_der_pol_amplitude_envelope


def test_vdp_limit_cycle():
    t = np.array([0.0, 1000.0])
    A = van_der_pol_amplitude_envelope(A0=0.5, eps=0.1, t=t)
    assert np.isclose(A[0], 0.5)
    assert np.isclose(A[-1], 2.0, atol=1e-3)
