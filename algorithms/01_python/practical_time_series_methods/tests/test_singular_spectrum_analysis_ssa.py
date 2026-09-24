import numpy as np
from singular_spectrum_analysis_ssa import ssa_decompose


def test_ssa():
    series = np.sin(np.linspace(0, 10, 50))
    U, s, Vt = ssa_decompose(series, L=15)
    assert len(s) == 15
    assert s[0] >= s[1]
