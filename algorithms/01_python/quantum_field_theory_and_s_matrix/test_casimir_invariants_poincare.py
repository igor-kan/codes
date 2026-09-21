import numpy as np
from casimir_invariants_poincare import mass_casimir, pauli_lubanski_spin_casimir


def test_poincare_casimirs():
    m = 0.938  # proton mass in GeV
    s = 0.5    # spin 1/2
    p = np.array([np.sqrt(m**2 + 10.0), 3.0, 1.0, 0.0])
    m_calc = np.sqrt(mass_casimir(p))
    assert np.isclose(m_calc, m, rtol=1e-4)

    w2 = pauli_lubanski_spin_casimir(m, s)
    expected_w2 = -(m**2) * 0.75
    assert np.isclose(w2, expected_w2)
