import numpy as np
from maxwell_boltzmann_velocity_dist import characteristic_speeds, mb_speed_pdf


def test_mb_speeds():
    speeds = characteristic_speeds(m=4.65e-26, T=300.0)
    assert speeds["v_mp"] < speeds["v_mean"] < speeds["v_rms"]
