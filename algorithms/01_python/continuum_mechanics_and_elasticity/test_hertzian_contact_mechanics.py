import numpy as np
from hertzian_contact_mechanics import hertzian_sphere_contact


def test_sphere_on_flat():
    # Sphere on flat (R2 -> infinity)
    R1 = 0.01  # 1 cm ball
    E1 = 210.0e9  # Steel
    nu1 = 0.3
    R2 = 1.0e10   # Flat plate
    E2 = 210.0e9
    nu2 = 0.3
    F = 100.0  # 100 N

    res = hertzian_sphere_contact(R1, E1, nu1, R2, E2, nu2, F)
    assert res["contact_radius"] > 0
    assert res["max_pressure"] > 0
    assert res["indentation"] > 0
