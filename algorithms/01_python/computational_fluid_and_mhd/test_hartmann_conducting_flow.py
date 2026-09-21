import numpy as np
from hartmann_conducting_flow import hartmann_number, hartmann_velocity_profile


def test_hartmann_profile():
    d = 0.05
    y = np.linspace(-d, d, 101)
    u0 = 1.0

    # Zero magnetic field limit -> parabolic
    u_pois = hartmann_velocity_profile(y, d, u0, Ha=0.0)
    assert np.isclose(u_pois[0], 0.0)
    assert np.isclose(u_pois[-1], 0.0)
    assert np.isclose(u_pois[50], u0)

    # High Ha -> boundary layer flattening
    u_flat = hartmann_velocity_profile(y, d, u0, Ha=20.0)
    # Average velocity in high Ha is closer to u0 in the center
    assert u_flat[40] > u_pois[40]
