import numpy as np
from klein_gordon_propagator import scalar_propagator_momentum, spacelike_propagator_decay


def test_scalar_propagator():
    m = 1.5
    # On-shell limit has large imaginary part
    p_onshell = np.array([np.sqrt(m**2 + 1.0), 1.0, 0.0, 0.0])
    prop = scalar_propagator_momentum(p_onshell, m, epsilon=1e-4)
    assert abs(prop.imag) > 1e3

    # Spacelike decay
    r1 = 2.0
    r2 = 4.0
    val1 = spacelike_propagator_decay(r1, m)
    val2 = spacelike_propagator_decay(r2, m)
    assert val1 > val2
