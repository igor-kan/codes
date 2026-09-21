import numpy as np
from passarino_veltman_reduction import a0_scalar, b0_feynman_parametric


def test_pv_integrals():
    m_sq = 4.0
    a0 = a0_scalar(m_sq, mu_sq=1.0, eps=1e-3)
    assert a0.real > 0

    b0 = b0_feynman_parametric(p_sq=1.0, m1_sq=2.0, m2_sq=2.0)
    assert np.isfinite(b0)
