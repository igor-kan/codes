import numpy as np
from optimal_order_execution_almgren import optimal_execution_trajectory


def test_almgren_execution():
    X0 = 100000.0
    traj = optimal_execution_trajectory(X0, T=1.0, N=10, gamma_perm=2e-7, eta_temp=1e-6, sigma=0.3, lam_risk=1e-5)
    assert np.isclose(traj[0], X0)
    assert np.isclose(traj[-1], 0.0)
    # Monotonically decreasing inventory
    assert np.all(np.diff(traj) <= 0.0)
