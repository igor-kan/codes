import numpy as np
from bose_einstein_condensation import condensate_fraction


def test_bec_fraction():
    assert condensate_fraction(0.0, 100.0) == 1.0
    assert condensate_fraction(100.0, 100.0) == 0.0
    assert np.isclose(condensate_fraction(50.0, 100.0), 1.0 - (0.5)**1.5)
