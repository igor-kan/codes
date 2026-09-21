import numpy as np
from shallow_water_1d_riemann import shallow_water_flux, roe_wave_speeds, G


def test_dam_break_speeds():
    # Left reservoir deep hL = 10m, right reservoir shallow hR = 1m
    hL, uL = 10.0, 0.0
    hR, uR = 1.0, 0.0

    lam1, lam2 = roe_wave_speeds(hL, uL, hR, uR)
    # Left wave propagates backward (negative), right wave forward (positive)
    assert lam1 < 0.0
    assert lam2 > 0.0

    f1, f2 = shallow_water_flux(hL, 0.0)
    assert f1 == 0.0
    assert np.isclose(f2, 0.5 * G * hL**2)
