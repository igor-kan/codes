import numpy as np
from running_coupling_qed import qed_running_alpha, qed_landau_pole_energy, ALPHA_0, M_E


def test_qed_running():
    # At Z boson mass M_Z = 91.1876 GeV, alpha runs to ~ 1/128
    m_z_sq = 91.1876**2
    alpha_mz = qed_running_alpha(m_z_sq)
    assert alpha_mz > ALPHA_0
    assert 1.0 / 137.0 < alpha_mz < 1.0 / 133.0

    # Landau pole log10 is around 280
    log_pole = qed_landau_pole_energy()
    assert log_pole > 200
