import numpy as np
from cylindrical_thick_pipe_lame import lame_cylinder_stresses


def test_lame_boundary_conditions():
    a = 0.1  # 10 cm inner
    b = 0.2  # 20 cm outer
    Pi = 10.0e6  # 10 MPa internal
    Po = 1.0e6   # 1 MPa external

    # At inner wall r = a, sigma_r = -Pi
    sr_a, sth_a = lame_cylinder_stresses(a, b, Pi, Po, a)
    assert np.isclose(sr_a, -Pi)

    # At outer wall r = b, sigma_r = -Po
    sr_b, sth_b = lame_cylinder_stresses(a, b, Pi, Po, b)
    assert np.isclose(sr_b, -Po)

    # Maximum hoop stress is at inner bore r = a
    assert sth_a > sth_b
