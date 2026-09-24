import numpy as np
from weno5_hyperbolic_shock_capturing import weno5_weights


def test_weno5():
    # Constant input should reconstruct exact constant
    val = weno5_weights(2.0, 2.0, 2.0, 2.0, 2.0)
    assert np.isclose(val, 2.0)
