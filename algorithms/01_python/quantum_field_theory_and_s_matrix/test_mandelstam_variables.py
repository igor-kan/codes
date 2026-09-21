import numpy as np
from mandelstam_variables import calculate_mandelstam, verify_mandelstam_sum, cm_scattering_angles


def test_mandelstam_kinematics():
    m = 0.511  # electron mass in MeV
    s = 10.0
    theta = np.pi / 3.0

    t, u = cm_scattering_angles(s, m, theta)
    assert verify_mandelstam_sum(s, t, u, (m, m, m, m))
    assert t <= 0.0
    assert u <= 0.0
