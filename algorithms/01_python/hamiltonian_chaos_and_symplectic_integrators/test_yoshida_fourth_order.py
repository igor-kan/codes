import numpy as np
from yoshida_fourth_order import yoshida4_integrate


def test_yoshida_fourth_order_accuracy():
    q0 = np.array([1.0])
    p0 = np.array([0.0])
    E0 = 0.5 * (q0[0]**2 + p0[0]**2)

    times, q_t, p_t = yoshida4_integrate(q0, p0, (0.0, 50.0), 500, lambda q: -q)
    energies = 0.5 * (q_t[:, 0]**2 + p_t[:, 0]**2)
    max_err = np.max(np.abs(energies - E0))

    # 4th-order method has much tighter energy conservation than 2nd-order Verlet
    assert max_err < 1e-5
