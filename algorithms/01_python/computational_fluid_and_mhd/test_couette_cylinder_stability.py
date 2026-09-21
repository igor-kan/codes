import numpy as np
from couette_cylinder_stability import rayleigh_stability_criterion, couette_centrifugal_parameter


def test_couette_stability():
    r1 = 0.1
    r2 = 0.12
    # Inner rotating, outer stationary -> unstable according to Rayleigh
    assert not rayleigh_stability_criterion(r1, 10.0, r2, 0.0)

    # Outer rotating faster than r1^2/r2^2 * omega1 -> stable
    assert rayleigh_stability_criterion(r1, 0.0, r2, 10.0)
