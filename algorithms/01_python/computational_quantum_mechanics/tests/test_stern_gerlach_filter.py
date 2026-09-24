import numpy as np
from stern_gerlach_filter import spin_state_along_direction, transition_probability


def test_stern_gerlach():
    z_plus = spin_state_along_direction(0.0, 0.0)
    x_plus = spin_state_along_direction(np.pi / 2.0, 0.0)
    P = transition_probability(z_plus, x_plus)
    assert np.isclose(P, 0.5)
