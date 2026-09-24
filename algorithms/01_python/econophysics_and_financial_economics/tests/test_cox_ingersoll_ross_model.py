import numpy as np
from cox_ingersoll_ross_model import cir_feller_satisfied, cir_simulate


def test_cir():
    assert cir_feller_satisfied(k=1.0, theta=0.05, sigma=0.2)
    rates = cir_simulate(0.04, 1.0, 0.05, 0.1, 1.0, 100)
    assert np.all(rates >= 0.0)
