import numpy as np
from poincare_recurrence import find_poincare_recurrence


def test_periodic_recurrence():
    # Simple harmonic orbit with period 100 steps
    t = np.linspace(0, 10.0 * np.pi, 501)
    traj = np.column_stack([np.cos(t), np.sin(t)])
    step = find_poincare_recurrence(traj, epsilon=0.05)
    assert step > 0
