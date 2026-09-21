import numpy as np
from melnikov_integral_chaos import duffing_melnikov_function, is_melnikov_chaotic


def test_melnikov_threshold():
    omega = 1.0
    delta = 0.2  # damping
    # Low forcing -> no chaos
    assert not is_melnikov_chaotic(gamma=0.01, delta=delta, omega=omega)
    # High forcing -> transverse homoclinic crossings
    assert is_melnikov_chaotic(gamma=0.5, delta=delta, omega=omega)
