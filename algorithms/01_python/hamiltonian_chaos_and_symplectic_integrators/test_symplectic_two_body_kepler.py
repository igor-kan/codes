import numpy as np
from symplectic_two_body_kepler import kepler_force, angular_momentum_2d, runge_lenz_vector_2d
from yoshida_fourth_order import yoshida4_step


def test_kepler_invariants():
    # Eccentric orbit e = 0.5: at perihelion r_p = a * (1 - e) = 0.5
    # v_p = sqrt(GM * (1 + e) / (a * (1 - e))) = sqrt(1.5 / 0.5) = sqrt(3)
    q = np.array([0.5, 0.0])
    p = np.array([0.0, np.sqrt(3.0)])
    L0 = angular_momentum_2d(q, p)
    A0 = runge_lenz_vector_2d(q, p)

    dt = 0.01
    for _ in range(500):
        q, p = yoshida4_step(q, p, dt, kepler_force)

    L_final = angular_momentum_2d(q, p)
    A_final = runge_lenz_vector_2d(q, p)

    assert np.isclose(L_final, L0, atol=1e-8)
    assert np.allclose(A_final, A0, atol=1e-5)
